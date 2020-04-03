import logging
import logging.handlers
import signal
import threading
import types
from typing import List, Optional

from interdaktive.config import Config
from interdaktive.hardware import Hardware
from interdaktive.state_machine import StateMachine, Transitions

if __name__ == '__main__':
    # Load up the configuration from command line arguments.
    config: Config = Config.from_args()

    # Configure logging.
    handlers: Optional[List[logging.Handler]] = None
    if config.log_file_path is not None:
        handlers = [logging.handlers.RotatingFileHandler(
            filename=config.log_file_path,
            maxBytes=int(16 * 2e10),
            backupCount=3,
        )]
    logging.basicConfig(
        format='%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s',
        handlers=handlers,
        level=logging.DEBUG,
    )

    logger = logging.getLogger(__package__)
    logger.debug(vars(config))

    # Instantiate hardware objects.
    hardware = Hardware(config)

    # Create the state machine.
    state_machine = StateMachine(config, hardware)

    # Wire the state machine up to external events.
    def handle_signal(signal_number: signal.Signals, frame: types.FrameType) -> None:
        state_machine[Transitions.signal_received](signal_number=signal_number, frame=frame)

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    hardware.motion_sensor.when_motion = state_machine[Transitions.motion_detected]
    hardware.motion_sensor.when_no_motion = state_machine[Transitions.motion_undetected]

    if hardware.control_button:
        hardware.control_button.when_released = state_machine[Transitions.control_button_released]
        hardware.control_button.when_held = state_machine[Transitions.control_button_held]

    # Start the web server.
    # web_server = WebServer(config, state_machine)
    # web_server.serve_forever()

    # Transition the state machine to operational mode and run until signalled to quit.
    state_machine[Transitions.started]()
    signal.pause()
