import collections
import logging
import os
import subprocess
import time
import typing

from transitions.extensions import GraphMachine as Machine  # type: ignore
from transitions.extensions.states import Timeout  # type: ignore
from transitions.extensions.states import add_state_features  # type: ignore

from interdaktive.config import Config

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('transitions').setLevel(logging.DEBUG)


States = collections.namedtuple('States', [
    'asleep',
    'awake',
    'idle',
    'shutting',
    'starting',
    'stopping',
])
states = States(
    asleep='asleep',
    awake='awake',
    idle='idle',
    shutting='shutting',
    starting='starting',
    stopping='stopping',
)


Transitions = collections.namedtuple('Transitions', [
    'button_held',
    'button_released',
    'idle_timed_out',
    'motion_detected',
    'no_motion_detected',
    'signal_received',
    'started',
])
transitions = Transitions(
    button_held='button_held',
    button_released='button_released',
    idle_timed_out='idle_timed_out',
    motion_detected='motion_detected',
    no_motion_detected='no_motion_detected',
    signal_received='signal_received',
    started='started',
)


@add_state_features(Timeout)
class StateMachine(Machine):
    __config: Config
    # __idle_timer: typing.Union[threading.Timer, None]

    def __init__(self, config: Config):
        enhanced_states = []
        for state in states:
            if state == states.idle:
                enhanced_states.append({
                    'name': state,
                    'timeout': config.sleep_delay_seconds,
                    'on_timeout': 'on_idle_timeout'
                })
            else:
                enhanced_states.append(state)

        super().__init__(
            self,
            states=enhanced_states,
            initial=states.starting,
            # machine_context=threading.RLock(),
            auto_transitions=False,
            show_conditions=True,
            show_state_attributes=True,
        )

        self.__config = config
        self.__idle_timer = None

        # Add transitions for starting, stopping, and shutting down.
        self.add_transition(transitions.started, states.starting, states.asleep,
                            after=[self.running_led_on, self.display_off])

        self.add_transition(transitions.signal_received, '*', states.stopping,
                            after=lambda *args, **kwargs: os._exit(0))

        self.add_transition(transitions.button_held, '*', states.shutting,
                            after=lambda *args, **kwargs: subprocess.run('shutdown now', shell=True))

        # Add transitions between asleep, awake, and idle.
        self.add_transition(transitions.motion_detected, [states.asleep, states.idle], states.awake,
                            prepare=self.motion_led_on,
                            conditions='is_waking_time',  # A string is specified so that it shows up in the diagram
                            after=self.display_on)

        self.add_transition(transitions.no_motion_detected, states.awake, states.idle,
                            prepare=self.motion_led_off)

        self.add_transition(transitions.idle_timed_out, states.idle, states.asleep,
                            after=self.display_off)

        self.add_transition(transitions.button_released, states.asleep, states.idle,
                            after=self.display_on)
        self.add_transition(transitions.button_released, [states.awake, states.idle], states.asleep,
                            after=self.display_off)

    def __getitem__(self, key: str) -> typing.Callable[[], None]:
        return getattr(self, getattr(transitions, key))

    def save_graph_to_file(self) -> None:
        self.machine_attributes['ratio'] = '0.33'
        graph = self.get_graph(force_new=True, title='')
        graph.draw('doc/state-machine.png', prog='dot')

    # def on_enter_idle(self, *args, **kwargs) -> None:
    #     if self.__idle_timer is not None:
    #         self.__idle_timer.cancel()
    #         self.__idle_timer = None

    #     def handler():
    #         try:
    #             self[transitions.idle_timed_out]()
    #         except:
    #             print('error')
    #         finally:
    #             print('done')

    #     self.__idle_timer = threading.Timer(self.__config.sleep_delay_seconds, handler)
    #     self.__idle_timer.start()

    # def on_exit_idle(self, *args, **kwargs) -> None:
    #     if self.__idle_timer is not None:
    #         self.__idle_timer.cancel()
    #         self.__idle_timer = None

    def on_idle_timeout(self) -> None:
        print('on_idle_timeout')
        self[transitions.idle_timed_out]()

    def display_off(self) -> None:
        self.__config.display.off()

    def display_on(self) -> None:
        self.__config.display.on()

    def motion_led_off(self) -> None:
        if self.__config.motion_led:
            self.__config.motion_led.off()

    def motion_led_on(self) -> None:
        if self.__config.motion_led:
            self.__config.motion_led.on()

    def running_led_on(self) -> None:
        if (self.__config.running_led):
            self.__config.running_led.on()

    def is_waking_time(self) -> bool:
        now: time.struct_time = time.localtime()
        return (
            (
                now.tm_hour > self.__config.waking_time_begin.tm_hour or
                (now.tm_hour == self.__config.waking_time_begin.tm_hour and now.tm_min >= self.__config.waking_time_begin.tm_min)
            ) and
            not (
                now.tm_hour > self.__config.waking_time_end.tm_hour or
                (now.tm_min == self.__config.waking_time_end.tm_min and now.tm_min >= self.__config.waking_time_end.tm_min)
            )
        )
