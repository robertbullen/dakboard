import collections
import logging
import os
import subprocess
import time
import typing
from dataclasses import astuple, dataclass, fields

from transitions import Machine  # type: ignore
from transitions.extensions.states import Timeout  # type: ignore
from transitions.extensions.states import add_state_features  # type: ignore

from interdaktive.config import Config

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('transitions').setLevel(logging.INFO)


@dataclass(frozen=True)
class States:
    asleep: str = 'asleep'
    awake: str = 'awake'
    idle: str = 'idle'
    shutting: str = 'shutting'
    starting: str = 'starting'
    stopping: str = 'stopping'

    def __iter__(self) -> typing.Iterator[str]:
        return iter(astuple(self))


@dataclass(frozen=True)
class Transitions:
    button_held: str = 'button_held'
    button_released: str = 'button_released'
    idle_timed_out: str = 'idle_timed_out'
    motion_detected: str = 'motion_detected'
    no_motion_detected: str = 'no_motion_detected'
    signal_received: str = 'signal_received'
    started: str = 'started'

    def __iter__(self) -> typing.Iterator[str]:
        return iter(astuple(self))


class StateMachine(object):
    config: Config
    machine: Machine

    def __init__(self, config: Config, machine_class, **kwargs):
        self.config = config

        # The idle state requires a timeout feature, so add it while converting the `states` tuple
        # to a list.
        states_with_features: typing.List[typing.Union[typing.Dict, str]] = []
        for state in States():
            if state == States.idle:
                states_with_features.append({
                    'name': state,
                    'timeout': self.config.sleep_delay_seconds,
                    'on_timeout': self.on_idle_timeout.__name__  # A string is required here.
                })
            else:
                states_with_features.append(state)

        # Call the constructor of one of the multitude of possible transitions' Machine mixins.
        machine_class_with_features = add_state_features(Timeout)(machine_class)
        self.machine = machine_class_with_features(
            model=self,
            states=states_with_features,
            initial=States.starting,
            auto_transitions=False,
            **kwargs,
        )

        # Add transitions for starting, stopping, and shutting down.
        self.machine.add_transition(Transitions.started, States.starting, States.asleep,
                                    after=[self.running_led_on, self.display_off])

        self.machine.add_transition(Transitions.signal_received, '*', States.stopping,
                                    after=self.quit)

        self.machine.add_transition(Transitions.button_held, '*', States.shutting,
                                    after=self.shutdown)

        # Add transitions between asleep, awake, and idle.
        self.machine.add_transition(Transitions.motion_detected, [States.idle, States.asleep], States.awake,
                                    prepare=self.motion_led_on,
                                    conditions=self.is_waking_time.__name__,  # A string is not required, but it won't show up on the diagram otherwise.
                                    after=self.display_on)

        self.machine.add_transition(Transitions.no_motion_detected, States.awake, States.idle,
                                    prepare=self.motion_led_off)
        self.machine.add_transition(Transitions.no_motion_detected, [States.idle, States.asleep], None,
                                    prepare=self.motion_led_off)

        self.machine.add_transition(Transitions.idle_timed_out, States.idle, States.asleep,
                                    after=self.display_off)

        self.machine.add_transition(Transitions.button_released, States.asleep, States.idle,
                                    after=self.display_on)
        self.machine.add_transition(Transitions.button_released, [States.awake, States.idle], States.asleep,
                                    after=self.display_off)

    def __getitem__(self, key: str) -> typing.Callable[[], None]:
        return getattr(self, getattr(Transitions, key))

    def quit(self, *args, **kwargs) -> None:
        os._exit(0)

    def shutdown(self, *args, **kwargs) -> None:
        subprocess.run('shutdown now', shell=True)

    def on_idle_timeout(self, *args, **kwargs) -> None:
        self[Transitions.idle_timed_out]()

    def display_off(self, *args, **kwargs) -> None:
        self.config.display.off()

    def display_on(self, *args, **kwargs) -> None:
        self.config.display.on()

    def motion_led_off(self, *args, **kwargs) -> None:
        if self.config.motion_led:
            self.config.motion_led.off()

    def motion_led_on(self, *args, **kwargs) -> None:
        if self.config.motion_led:
            self.config.motion_led.on()

    def running_led_on(self, *args, **kwargs) -> None:
        if (self.config.running_led):
            self.config.running_led.on()

    def is_waking_time(self, *args, **kwargs) -> bool:
        now: time.struct_time = time.localtime()
        return (
            (
                now.tm_hour > self.config.waking_time_begin.tm_hour or
                (now.tm_hour == self.config.waking_time_begin.tm_hour and now.tm_min >= self.config.waking_time_begin.tm_min)
            ) and
            not (
                now.tm_hour > self.config.waking_time_end.tm_hour or
                (now.tm_min == self.config.waking_time_end.tm_min and now.tm_min >= self.config.waking_time_end.tm_min)
            )
        )
