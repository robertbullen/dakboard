import collections
import functools
import logging
import os
import signal
import subprocess
import time
from dataclasses import astuple, dataclass, fields
from typing import (Any, Callable, Dict, Iterator, List, Optional, Tuple, Type,
                    Union, cast)

import gpiozero
from transitions import Machine
from transitions.extensions.states import Timeout, add_state_features

from interdaktive.config import Config
from interdaktive.hardware import Hardware

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('transitions').setLevel(logging.INFO)


@dataclass(frozen=True)
class States:
    starting: str = 'starting'

    stopping: str = 'stopping'
    shutting_down: str = 'shutting_down'

    awake: str = 'awake'
    timed_awake: str = 'timed_awake'
    forced_awake: str = 'forced_awake'

    forced_asleep: str = 'forced_asleep'
    asleep: str = 'asleep'

    def __iter__(self) -> Iterator[str]:
        return iter(astuple(self))


@dataclass(frozen=True)
class Transitions:
    started: str = 'started'

    button_held: str = 'button_held'
    button_released: str = 'button_released'

    motion_detected: str = 'motion_detected'
    motion_undetected: str = 'motion_undetected'

    timer_expired: str = 'timer_expired'

    signal_received: str = 'signal_received'

    def __iter__(self) -> Iterator[str]:
        return iter(astuple(self))


class StateMachine(object):
    config: Config
    hardware: Hardware
    machine: Machine

    def __init__(self, config: Config, hardware: Hardware, machine_class: Type[Machine], **kwargs: Any) -> None:
        self.config = config
        self.hardware = hardware

        # A few states require timeouts, so add the feature to them while converting all the
        # `States` to a list.
        states_with_features: List[Union[Dict[str, Union[int, str]], str]] = []
        for state in States():
            if state == States.forced_asleep or state == States.forced_awake or state == States.timed_awake:
                states_with_features.append({
                    'name': state,
                    'timeout': self.config.timer_seconds,
                    'on_timeout': Transitions.timer_expired
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

        # Add transitions for process control: starting, stopping, and shutting_down.
        self.machine.add_transition(Transitions.started, States.starting, States.asleep,
                                    prepare=self.hardware.running_led_on)

        self.machine.add_transition(Transitions.signal_received, '*', States.stopping,
                                    after=[
                                        self.hardware.motion_led_off,
                                        self.hardware.display_off,
                                        self.hardware.running_led_off,
                                        self.quit,
                                    ])

        self.machine.add_transition(Transitions.button_held, '*', States.shutting_down,
                                    after=self.shutdown)

        # Add transitions for motion (un)detected.
        self.machine.add_transition(Transitions.motion_detected, [States.asleep, States.timed_awake, States.awake], States.awake,
                                    prepare=self.hardware.motion_led_on,
                                    # A string is not required here, but it won't show up on a diagram otherwise.
                                    conditions=self.is_waking_hours.__name__)
        self.machine.add_transition(Transitions.motion_detected, '*', None)

        self.machine.add_transition(Transitions.motion_undetected, States.awake, States.timed_awake,
                                    prepare=self.hardware.motion_led_off)
        self.machine.add_transition(Transitions.motion_undetected, States.asleep, None,
                                    prepare=self.hardware.motion_led_off)
        self.machine.add_transition(Transitions.motion_undetected, '*', None)

        self.machine.add_transition(Transitions.timer_expired, States.timed_awake, States.asleep)

        # Add transitions into and out of the forced states.
        self.machine.add_transition(Transitions.button_released, [States.asleep, States.forced_asleep], States.forced_awake)
        self.machine.add_transition(Transitions.button_released, [States.forced_awake, States.timed_awake, States.awake], States.forced_asleep)
        self.machine.add_transition(Transitions.button_released, '*', None)

        self.machine.add_transition(Transitions.timer_expired, [States.forced_asleep, States.forced_awake], States.asleep)

    def __getitem__(self, key: str) -> Callable[..., None]:
        return cast(Callable[..., None], getattr(self, getattr(Transitions, key)))

    # Transition Condition Predicates

    def is_waking_hours(self, *args: Any, **kwargs: Any) -> bool:
        def gteq(left: time.struct_time, right: time.struct_time) -> bool:
            return left.tm_hour > right.tm_hour or (left.tm_hour == right.tm_hour and left.tm_min >= right.tm_min)

        def lt(left: time.struct_time, right: time.struct_time) -> bool:
            return not gteq(left, right)

        now: time.struct_time = time.localtime()
        return gteq(now, self.config.waking_hours_begin) and lt(now, self.config.waking_hours_end)

    # Transition Callbacks

    def quit(self, *args: Any, **kwargs: Any) -> None:
        signal_number = kwargs['signal_number']
        signal_name = signal.strsignal(signal_number) if hasattr(signal, 'strsignal') else signal_number  # type: ignore
        print('Received signal {0}; quiting'.format(signal_name))
        os._exit(0)

    def shutdown(self, *args: Any, **kwargs: Any) -> None:
        subprocess.run('shutdown now', shell=True)

    # State Event Handlers

    def on_enter_asleep(self, *args: Any, **kwargs: Any) -> None:
        self.hardware.display_off()

    def on_enter_awake(self, *args: Any, **kwargs: Any) -> None:
        self.hardware.display_on()

    def on_enter_forced_awake(self, *args: Any, **kwargs: Any) -> None:
        self.hardware.motion_led_blink()
        self.hardware.display_on()

    def on_exit_forced_awake(self, *args: Any, **kwargs: Any) -> None:
        self.hardware.motion_led_off()

    def on_enter_forced_asleep(self, *args: Any, **kwargs: Any) -> None:
        self.hardware.motion_led_blink()
        self.hardware.display_off()

    def on_exit_forced_asleep(self, *args: Any, **kwargs: Any) -> None:
        self.hardware.motion_led_off()
