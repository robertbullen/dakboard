import signal
import threading

from interdaktive.config import Config
from interdaktive.state_machine import StateMachine, transitions

# This is handy for logging.
# def qualified_method_name(method) -> str:
#     clazz = method.__self__.__class__
#     return '{0}::{1}'.format(clazz.__name__, method.__name__)


if __name__ == '__main__':
    # Load up the configuration from command line arguments.
    config: Config = Config.from_args()
    print(vars(config))

    # Create the state machine and wire it up to external events.
    state_machine = StateMachine(config)

    config.motion_sensor.when_motion = state_machine.motion_detected
    config.motion_sensor.when_no_motion = state_machine.no_motion_detected

    if config.control_button:
        config.control_button.when_released = state_machine.button_released
        config.control_button.when_held = state_machine.button_held

    signal.signal(signal.SIGINT, state_machine.signal_received)
    signal.signal(signal.SIGTERM, state_machine.signal_received)

    # Transition to operational mode.
    state_machine[transitions.started]()
    state_machine[transitions.button_released]()
    state_machine.save_graph_to_file()

    signal.pause()
