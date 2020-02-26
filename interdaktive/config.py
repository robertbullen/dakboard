import argparse
import functools
import time
from typing import Optional, cast

import gpiozero

import interdaktive.display as display
from interdaktive.display import Display


class Config(argparse.Namespace):
    control_button: Optional[gpiozero.Button]
    display: Display
    export_diagram_file_path: Optional[str]
    motion_led: Optional[gpiozero.LED]
    motion_sensor: gpiozero.MotionSensor
    running_led: Optional[gpiozero.LED]
    server_port: int
    timer_seconds: int
    waking_hours_begin: time.struct_time
    waking_hours_end: time.struct_time

    @staticmethod
    def from_args() -> 'Config':
        parser = argparse.ArgumentParser(
            epilog='gpiozero pin numbering format is described here: https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering',
            prog='python3 -m interdaktive',
        )

        def parse_display_type(arg: str) -> Display:
            if arg == 'cec':
                return display.cec
            if arg == 'mock':
                return display.mock
            if arg == 'video-core':
                return display.video_core
            raise ValueError(arg)

        def parse_time(arg: str) -> time.struct_time:
            try:
                # 24:00 is not allowed by strptime, but it is allowed by this script. It's the one
                # and only illegal time value, so just create a struct_time by hand in that case.
                result: time.struct_time
                if arg == '24:00':
                    result = time.struct_time((1900, 1, 1, 24, 0, 0, 0, 1, -1))
                else:
                    result = time.strptime(arg, '%H:%M')
                return result
            except ValueError:
                raise argparse.ArgumentTypeError("'{0}' is not a valid 24-hour clock formatted time".format(arg))

        # Required arguments.
        parser.add_argument(
            '--motion-sensor-pin',
            default=None,
            dest='motion_sensor',
            help='The GPIO pin (in gpiozero format) to which the motion sensor is attached.',
            metavar='MOTION_SENSOR_PIN',
            required=True,
            type=gpiozero.MotionSensor,
        )

        # Optional arguments.
        parser.add_argument(
            '--control-button-pin',
            default=None,
            dest='control_button',
            help='The GPIO pin (in gpiozero format) to which an optional control button is attached. Pressing the button will forcefully turn on the display, even outside of waking times. Holding the button for 5 seconds will shutdown the system.',
            metavar='CONTROL_BUTTON_PIN',
            type=functools.partial(gpiozero.Button, hold_time=5),
        )

        parser.add_argument(
            '--display-type',
            choices=[display.cec, display.mock, display.video_core],
            default='video-core',
            dest='display',
            help='The type of display that is connected, which determines how it is put to sleep and awakened. A "video-core" display simply responds to the HDMI signal turning off and on; e.g. a computer display. A "cec" display responds to HDMI-CEC commands; e.g. a TV.',
            metavar='DISPLAY_TYPE',
            type=parse_display_type,
        )

        parser.add_argument(
            '--export-diagram-file-path',
            help='If provided, a PNG diagram of the internal state machine will be generated at the given path.',
            type=str,
        )

        parser.add_argument(
            '--motion-led-pin',
            dest='motion_led',
            help='The GPIO pin (in gpiozero format) to which an optional motion indicator LED is attached.',
            metavar='MOTION_LED_PIN',
            type=gpiozero.LED,
        )

        parser.add_argument(
            '--running-led-pin',
            dest='running_led',
            help='The GPIO pin (in gpiozero format) to which an optional running indicator LED is attached.',
            metavar='RUNNING_LED_PIN',
            type=gpiozero.LED,
        )

        parser.add_argument(
            '--server-port',
            default=8088,
            help='The port on which to serve the status web site.',
            type=int,
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

        return parser.parse_args(namespace=Config())
