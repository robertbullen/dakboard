import argparse
import time


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
    control_button_pin: str
    display_type: str
    motion_led_pin: str
    motion_sensor_pin: str
    running_led_pin: str
    timer_seconds: int
    waking_hours_begin: time.struct_time
    waking_hours_end: time.struct_time
    web_server_port: int

    @staticmethod
    def from_args() -> 'Config':
        parser = argparse.ArgumentParser(
            epilog='gpiozero pin numbering format is described here: https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering',
            prog='python3 -m interdaktive',
        )

        # Required arguments.
        parser.add_argument(
            '--motion-sensor-pin',
            default=None,
            help='The GPIO pin (in gpiozero format) to which the motion sensor is attached.',
            required=True,
        )

        # Optional arguments.
        parser.add_argument(
            '--control-button-pin',
            default=None,
            help='The GPIO pin (in gpiozero format) to which an optional control button is attached. Pressing the button will forcefully turn on the display, even outside of waking times. Holding the button for 5 seconds will shutdown the system.',
        )

        parser.add_argument(
            '--display-type',
            choices=['cec', 'mock', 'video-core'],
            default='video-core',
            help='The type of display that is connected, which determines how it is put to sleep and awakened. A "video-core" display simply responds to the HDMI signal turning off and on; e.g. a computer display. A "cec" display responds to HDMI-CEC commands; e.g. a TV.',
        )

        parser.add_argument(
            '--motion-led-pin',
            help='The GPIO pin (in gpiozero format) to which an optional motion indicator LED is attached.',
        )

        parser.add_argument(
            '--running-led-pin',
            help='The GPIO pin (in gpiozero format) to which an optional running indicator LED is attached.',
        )

        parser.add_argument(
            '--timer-seconds',
            default=120,
            help='The length of time (in seconds) for the display to stay awake/asleep after detecting motion or the control button is pressed.',
            type=int,
        )

        parser.add_argument(
            '--waking-hours-begin',
            default='00:00',
            help='The beginning of the daily period (in 24-hour clock format; e.g. 06:00) when waking the display is allowed.',
            type=parse_time,
        )

        parser.add_argument(
            '--waking-hours-end',
            default='24:00',
            help='The beginning of the daily period (in 24-hour clock format; e.g. 22:00) when waking the display is allowed.',
            type=parse_time,
        )

        parser.add_argument(
            '--web-server-port',
            default=8088,
            help='The port on which to serve the status web site.',
            type=int,
        )

        return parser.parse_args(namespace=Config())
