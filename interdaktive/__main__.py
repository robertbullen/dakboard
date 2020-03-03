import signal
import threading
import types

from transitions.extensions import GraphMachine

from interdaktive.config import Config
from interdaktive.hardware import Hardware
from interdaktive.state_machine import StateMachine, Transitions
from interdaktive.web_server import WebServer

if __name__ == '__main__':
    # Load up the configuration from command line arguments.
    config: Config = Config.from_args()
    print(vars(config))

    hardware = Hardware(config)

    # Create the state machine.
    state_machine = StateMachine(
        config,
        hardware,
        GraphMachine,
        show_conditions=True,
        show_state_attributes=True,
        title='Interdaktive State Machine',
    )

    # Wire the state machine up to external events.
    def handle_signal(signal_number: signal.Signals, frame: types.FrameType) -> None:
        state_machine[Transitions.signal_received](signal_number=signal_number, frame=frame)

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    hardware.motion_sensor.when_motion = state_machine[Transitions.motion_detected]
    hardware.motion_sensor.when_no_motion = state_machine[Transitions.motion_undetected]

    if hardware.control_button:
        hardware.control_button.when_released = state_machine[Transitions.button_released]
        hardware.control_button.when_held = state_machine[Transitions.button_held]

    # Start the web server.
    web_server = WebServer(config, state_machine)
    web_server.serve_forever()

    # Transition the state machine to operational mode and run until signalled to quit.
    state_machine[Transitions.started]()
    signal.pause()
