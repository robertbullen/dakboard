import argparse
import time
from typing import Optional


def parse_time(value: str) -> time.struct_time:
    try:
        # 24:00 is not allowed by strptime, but it is accepted by this class. It's the one
        # and only illegal time value, so just create a `struct_time` by hand in that case.
        result: time.struct_time
        if value == '24:00':
            result = time.struct_time((1900, 1, 1, 24, 0, 0, 0, 1, -1))
        else:
            result = time.strptime(value, '%H:%M')
        return result
    except ValueError:
        raise argparse.ArgumentTypeError("'{0}' is not a valid 24-hour clock formatted time".format(value))


def format_time(value: time.struct_time) -> str:
    try:
        result: str
        if value == time.struct_time((1900, 1, 1, 24, 0, 0, 0, 1, -1)):
            result = '24:00'
        else:
            result = time.strftime('%H:%M', value)
        return result
    except TypeError:
        raise argparse.ArgumentTypeError("'{0}' is not a valid 24-hour clock time struct".format(value))


class Config(argparse.Namespace):
    # Hardware.
    control_button_pin: Optional[str]
    display_type: str
    motion_led_pin: Optional[str]
    motion_sensor_pin: str
    running_led_pin: Optional[str]

    # Timing.
    timer_seconds: int
    waking_hours_begin: time.struct_time
    waking_hours_end: time.struct_time

    # Output.
    log_file_path: Optional[str]
    state_diagram_file_path: Optional[str]

    @staticmethod
    def from_args() -> 'Config':
        parser = argparse.ArgumentParser(prog='python3 -m interdaktive')

        hardware_group = parser.add_argument_group(
            'hardware arguments',
            (
                "GPIO pins must be specified in gpiozero pin numbering format, which is described "
                "at https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering."
            )
        )

        hardware_group.add_argument(
            '--motion-sensor-pin',
            help=(
                "The GPIO pin to which the motion sensor is attached. Detecting motion is this "
                "package's raison d'être, and no reasonable default can be assumed, so this is the "
                "one and only required argument."
            ),
            required=True,
        )

        hardware_group.add_argument(
            '--control-button-pin',
            help=(
                "The GPIO pin to which an optional control button is attached. Pressing the button "
                "will forcibly toggle the display, even outside of waking hours. Holding the "
                "button for 5 seconds will shutdown the system."
            ),
        )

        hardware_group.add_argument(
            '--display-type',
            choices=['cec', 'mock', 'video-core'],
            default='video-core',
            help=(
                "The type of display that is connected, which determines how it is put to sleep and "
                "awakened. A 'video-core' display simply responds to the HDMI signal turning off "
                "and on; e.g. a computer monitor. A 'cec' display responds to HDMI-CEC commands; "
                "e.g. a TV. A 'mock' display is useful for testing and simply outputs its state "
                "changes to the console."
            ),
        )

        hardware_group.add_argument(
            '--motion-led-pin',
            help='The GPIO pin to which an optional motion indicator LED is attached.',
        )

        hardware_group.add_argument(
            '--running-led-pin',
            help='The GPIO pin to which an optional running indicator LED is attached.',
        )

        timing_group = parser.add_argument_group('timing arguments')

        timing_group.add_argument(
            '--timer-seconds',
            default=120,
            help=(
                "The length of time (in seconds) for the display to stay awake/asleep after "
                "detecting motion or the control button is pressed. Also the length of time that "
                "the display will remain in its forcibly toggled state after pressing the control "
                "button."
            ),
            type=int,
        )

        timing_group.add_argument(
            '--waking-hours-begin',
            default='00:00',
            help=(
                "The beginning of the daily period (in 24-hour clock format; e.g. 06:00) when "
                "detecting motion will wake the display."
            ),
            type=parse_time,
        )

        timing_group.add_argument(
            '--waking-hours-end',
            default='24:00',
            help=(
                "The end of the daily period (in 24-hour clock format; e.g. 22:00) when "
                "detecting motion will wake the display."
            ),
            type=parse_time,
        )

        output_group = parser.add_argument_group('output arguments')

        output_group.add_argument(
            '--log-file-path',
            help='The file path to which logging output will be written.',
        )

        output_group.add_argument(
            '--state-diagram-file-path',
            help='The file path to which state diagram images will be written.',
        )

        return parser.parse_args(namespace=Config())
