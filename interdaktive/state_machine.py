import collections
import logging
import os
import signal
import subprocess
import time
from dataclasses import astuple, dataclass, fields
from typing import (Any, Callable, Dict, Iterator, List, Optional, Tuple, Type,
                    Union, cast)

from transitions import Machine
from transitions.extensions.states import Timeout, add_state_features

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

    def __iter__(self) -> Iterator[str]:
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

    def __iter__(self) -> Iterator[str]:
        return iter(astuple(self))


class StateMachine(object):
    config: Config
    machine: Machine

    def __init__(self, config: Config, machine_class: Type[Machine], **kwargs: Any) -> None:
        self.config = config

        # The idle state requires a timeout feature, so add it while converting the `states` tuple
        # to a list.
        states_with_features: List[Union[Dict[str, Union[int, str]], str]] = []
        for state in States():
            if state == States.idle:
                states_with_features.append({
                    'name': state,
                    'timeout': self.config.idle_timeout_seconds,
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
                                    conditions=self.is_waking_hours.__name__,  # A string is not required here, but it won't show up on a diagram otherwise.
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

    def __getitem__(self, key: str) -> Callable[..., None]:
        return cast(Callable[..., None], getattr(self, getattr(Transitions, key)))

    def quit(self, *args: Any, **kwargs: Any) -> None:
        signal_number = kwargs['signal_number']
        signal_name = signal.strsignal(signal_number) if hasattr(signal, 'strsignal') else signal_number
        print('Received signal {0}; quiting'.format(signal_name))
        os._exit(0)

    def shutdown(self, *args: Any, **kwargs: Any) -> None:
        subprocess.run('shutdown now', shell=True)

    def on_idle_timeout(self, *args: Any, **kwargs: Any) -> None:
        self[Transitions.idle_timed_out]()

    def display_off(self, *args: Any, **kwargs: Any) -> None:
        self.config.display.off()

    def display_on(self, *args: Any, **kwargs: Any) -> None:
        self.config.display.on()

    def motion_led_off(self, *args: Any, **kwargs: Any) -> None:
        if self.config.motion_led:
            self.config.motion_led.off()

    def motion_led_on(self, *args: Any, **kwargs: Any) -> None:
        if self.config.motion_led:
            self.config.motion_led.on()

    def running_led_on(self, *args: Any, **kwargs: Any) -> None:
        if (self.config.running_led):
            self.config.running_led.on()

    def is_waking_hours(self, *args: Any, **kwargs: Any) -> bool:
        def gteq(left: time.struct_time, right: time.struct_time) -> bool:
            return left.tm_hour > right.tm_hour or (left.tm_hour == right.tm_hour and left.tm_min >= right.tm_min)

        def lt(left: time.struct_time, right: time.struct_time) -> bool:
            return not gteq(left, right)

        now: time.struct_time = time.localtime()
        return gteq(now, self.config.waking_hours_begin) and lt(now, self.config.waking_hours_end)
