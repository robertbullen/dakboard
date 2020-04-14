import logging
import logging.handlers
import re
import signal
import sys
import threading
import types
from typing import List, Optional, Pattern, Type

from interdaktive.config import Config
from interdaktive.hardware import Hardware
from interdaktive.state_machine import StateMachine, Transitions

if __name__ == '__main__':
    # Load up the configuration from command line arguments.
    config: Config = Config.from_args()

    # Configure logging to write to rotating files.
    handlers: Optional[List[logging.Handler]] = None
    if config.log_file_path is not None:
        handlers = [logging.handlers.RotatingFileHandler(
            filename=config.log_file_path,
            maxBytes=int(16 * 2**10),
            backupCount=3,
        )]
    logging.basicConfig(
        format='%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s',
        handlers=handlers,
        level=logging.DEBUG,
    )

    # Filter out a couple unwanted log messages from _transitions_.
    executed_save_state_diagram: Pattern[str] = re.compile(
        r'Executed machine finalize callback \'<function StateMachine\.__init__\.<locals>\.handle_finalize_event at 0x[0-9a-fA-F]+>\'.$'
    )
    returning_graph_model: Pattern[str] = re.compile(
        r'^Returning graph of the first model. In future releases, this method will return a combined graph of all models.$'
    )

    def filter(record: logging.LogRecord) -> bool:
        global executed_save_state_diagram
        global returning_graph_model

        return (
            executed_save_state_diagram.match(record.getMessage()) is None
            and returning_graph_model.match(record.getMessage()) is None
        )

    logging.getLogger('transitions.core').addFilter(filter)
    logging.getLogger('transitions.extensions.diagrams').addFilter(filter)

    # Log any unhandled exceptions.
    logger = logging.getLogger(__name__)

    def handle_unhandled_exception(
        exc_type: Type[BaseException],
        exc_value: BaseException,
        exc_traceback: types.TracebackType,
    ) -> None:
        global logger

        if issubclass(exc_type, KeyboardInterrupt):
            # Call the default hook.
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        logger.exception("Unhandled exception", exc_info=(exc_type, exc_value, exc_traceback))

    sys.excepthook = handle_unhandled_exception

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

    # Transition the state machine to operational mode and run until signalled to quit.
    state_machine[Transitions.started]()
    signal.pause()
