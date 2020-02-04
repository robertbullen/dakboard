import argparse
import signal
import subprocess
import sys
import threading
import time
import typing

import gpiozero  # type: ignore


# This is handy for logging.
def qualified_method_name(method) -> str:
    clazz = method.__self__.__class__
    return '{0}::{1}'.format(clazz.__name__, method.__name__)


# Declare and instantiate a class responsible for turning on/off the display.
class Display:
    __is_on: bool = False
    __lock: threading.Lock = threading.Lock()
    __off_command: str
    __on_command: str

    def __init__(self, turn_off_command: str, turn_on_command: str):
        print(qualified_method_name(self.__init__))  # type: ignore
        self.__off_command = turn_off_command
        self.__on_command = turn_on_command

    def off(self) -> None:
        self.__lock.acquire()
        try:
            print(qualified_method_name(self.off))
            if self.__is_on:
                # subprocess.run(self.__off_command, shell=True)
                self.__is_on = False
        finally:
            self.__lock.release()

    def on(self) -> None:
        self.__lock.acquire()
        try:
            print(qualified_method_name(self.on))
            if not self.__is_on:
                # subprocess.run(self.__on_command, shell=True)
                self.__is_on = True
        finally:
            self.__lock.release()

    @staticmethod
    def cec() -> 'Display':
        return Display('echo \'standby 0\' | cec-client -s -d 1', 'echo \'on 0\' | cec-client -s -d 1')

    @staticmethod
    def video_core() -> 'Display':
        return Display('vcgencmd display_power 0', 'vcgencmd display_power 1')


class Config(argparse.Namespace):
    display: Display
    motion_led: typing.Union[gpiozero.LED, None]
    motion_sensor: gpiozero.MotionSensor
    running_led: typing.Union[gpiozero.LED, None]
    sleep_delay_seconds: int
    waking_time_begin: time.struct_time
    waking_time_end: time.struct_time

    @staticmethod
    def create() -> 'Config':
        parser = argparse.ArgumentParser(
            epilog='gpiozero pin numbering format is described here: https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering')

        def parse_display_type(arg: str) -> Display:
            if arg == 'cec':
                return Display.cec()
            if arg == 'video-core':
                return Display.video_core()
            raise ValueError(arg)

        def parse_time(arg: str) -> time.struct_time:
            try:
                # 24:00 is not allowed by strptime, but it is allowed by this script. So create a
                # struct_time by hand in that case.
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
            help='The GPIO pin to which a motion sensor is attached',
            required=True,
            type=gpiozero.MotionSensor,
        )

        # Optional arguments.
        parser.add_argument(
            '--display-type',
            choices=['video-core', 'cec'],
            default='video-core',
            dest='display',
            help='The type of display that is connected, which determines how it is put to sleep and awakened. A "video-core" display simply responds to the HDMI signal turning off and on; e.g. a computer display. A "cec" display responds to HDMI-CEC commands; e.g. a TV.',
            type=parse_display_type,  # type: ignore
        )

        parser.add_argument(
            '--motion-led-pin',
            dest='motion_led',
            help='The GPIO pin (in gpiozero format) to which a motion indicator LED is attached',
            type=gpiozero.LED,
        )

        parser.add_argument(
            '--running-led-pin',
            dest='running_led',
            help='The GPIO pin (in gpiozero format) to which a running indicator LED is attached',
            type=gpiozero.LED,
        )

        parser.add_argument(
            '--sleep-delay-seconds',
            default=120,
            help='The length of time (in seconds) to keep the display awake after no motion is detected',
            type=int,
        )

        parser.add_argument(
            '--waking-time-begin',
            default='00:00',
            help='The beginning of the daily period (in 24-hour clock format; e.g. 06:00) where waking the display is allowed',
            type=parse_time,
        )

        parser.add_argument(
            '--waking-time-end',
            default='24:00',
            help='The beginning of the daily period (in 24-hour clock format; e.g. 22:00) where waking the display is allowed',
            type=parse_time,
        )

        return typing.cast(Config, parser.parse_args(namespace=Config()))

    def is_waking_time(self, now: time.struct_time) -> bool:
        return (
            (
                now.tm_hour > self.waking_time_begin.tm_hour or
                (now.tm_hour == self.waking_time_begin.tm_hour and now.tm_min >= self.waking_time_begin.tm_min)
            ) and
            not (
                now.tm_hour > self.waking_time_end.tm_hour or
                (now.tm_min == self.waking_time_end.tm_min and now.tm_min >= self.waking_time_end.tm_min)
            )
        )


def main() -> None:
    # Load up the configuration (from the command line arguments).
    config: Config = Config.create()

    # Turn on the running LED for as long as this script is executing.
    if config.running_led:
        config.running_led.on()

    # Turn on the display and schedule turning it off.
    config.display.on()

    sleep_timer: threading.Timer = threading.Timer(config.sleep_delay_seconds, config.display.off)
    sleep_timer.start()

    # Wire up some motion sensor event handlers to turn on and off the display.
    def when_motion():
        nonlocal config
        nonlocal sleep_timer

        if config.motion_led:
            config.motion_led.on()

        sleep_timer.cancel()

        if config.is_waking_time(time.localtime()):
            config.display.on()

    def when_no_motion():
        nonlocal config
        nonlocal sleep_timer

        if config.motion_led:
            config.motion_led.off()

        sleep_timer = threading.Timer(config.sleep_delay_seconds, config.display.off)
        sleep_timer.start()

    config.motion_sensor.when_motion = when_motion
    config.motion_sensor.when_no_motion = when_no_motion

    # Wire up a signal handler to clean up.
    def signal_handler(signal, frame) -> None:
        config.display.off()
        sys.exit()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Wait for an external signal to terminate this script.
    signal.pause()


main()
