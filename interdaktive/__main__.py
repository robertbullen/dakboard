import signal
import threading

from interdaktive.config import Config
from interdaktive.state_machine import StateMachine, transitions

if __name__ == '__main__':
    # Load up the configuration from command line arguments.
    config: Config = Config.from_args()
    print(vars(config))

    # Create the state machine.
    state_machine = StateMachine(config)
    state_machine.save_diagram_to_file('doc/state-machine.png')

    # Wire the state machine up to external events.
    signal.signal(signal.SIGINT, state_machine.signal_received)
    signal.signal(signal.SIGTERM, state_machine.signal_received)

    config.motion_sensor.when_motion = state_machine.motion_detected
    config.motion_sensor.when_no_motion = state_machine.no_motion_detected

    if config.control_button:
        config.control_button.when_released = state_machine.button_released
        config.control_button.when_held = state_machine.button_held

    # Transition the state machine to operational mode and run until signalled to quit.
    state_machine[transitions.started]()
    signal.pause()
