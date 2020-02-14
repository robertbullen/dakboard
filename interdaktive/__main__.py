import signal
import threading
import types

from interdaktive.config import Config
from interdaktive.state_machine import StateMachine, Transitions

if __name__ == '__main__':
    # Load up the configuration from command line arguments.
    config: Config = Config.from_args()
    print(vars(config))

    # Create the state machine.
    if config.export_diagram_file_path is not None:
        from transitions.extensions import GraphMachine
        state_machine = StateMachine(
            config,
            GraphMachine,
            show_conditions=True,
            show_state_attributes=True,
            title='Interdaktive State Machine'
        )
        state_machine.machine.machine_attributes['labelloc'] = 'top'
        state_machine.machine.machine_attributes['ratio'] = '0.33'
        state_machine.machine.get_graph(force_new=True).draw(config.export_diagram_file_path, prog='dot')
    else:
        from transitions import Machine
        state_machine = StateMachine(config, Machine)

    # Wire the state machine up to external events.
    def handle_signal(signal_number: signal.Signals, frame: types.FrameType) -> None:
        state_machine[Transitions.signal_received](signal_number=signal_number, frame=frame)

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    config.motion_sensor.when_motion = state_machine[Transitions.motion_detected]
    config.motion_sensor.when_no_motion = state_machine[Transitions.motion_undetected]

    if config.control_button:
        config.control_button.when_released = state_machine[Transitions.button_released]
        config.control_button.when_held = state_machine[Transitions.button_held]

    # Transition the state machine to operational mode and run until signalled to quit.
    state_machine[Transitions.started]()
    signal.pause()
