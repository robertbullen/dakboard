import signal
import subprocess
import sys
import time

import RPi.GPIO as gpio


def qualified_method_name(method) -> str:
    clazz = method.__self__.__class__
    return '{0}::{1}'.format(clazz.__name__, method.__name__)


# Declare and instantiate a class responsible for the GPIO pins.

class GpioPins:
    motion_detector = 11
    motion_indicator_led = 3
    power_indicator_led = 5

    def __init__(self):
        print(qualified_method_name(self.__init__))
        gpio.setwarnings(True)
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.motion_detector, gpio.IN)
        gpio.setup(self.motion_indicator_led, gpio.OUT, initial=gpio.LOW)
        gpio.setup(self.power_indicator_led, gpio.OUT, initial=gpio.HIGH)

    def cleanup(self) -> None:
        print(qualified_method_name(self.cleanup))
        gpio.cleanup()

    def read_motion_detector(self) -> bool:
        is_motion_detected = bool(gpio.input(self.motion_detector))
        print(qualified_method_name(self.read_motion_detector), is_motion_detected)
        return is_motion_detected

    def write_motion_indicator(self, is_motion_detected: bool) -> None:
        print(qualified_method_name(self.write_motion_indicator), is_motion_detected)
        gpio.output(self.motion_indicator_led, is_motion_detected)


# Declare and instantiate a class responsible for turning on/off the monitor.

class Monitor:
    __turn_off_command: str
    __turn_on_command: str
    __is_on: bool = False

    def __init__(self, turn_off_command: str, turn_on_command: str):
        print(qualified_method_name(self.__init__))
        self.__turn_off_command = turn_off_command
        self.__turn_on_command = turn_on_command

    def turn_off(self) -> None:
        print(qualified_method_name(self.turn_off))
        if self.__is_on:
            subprocess.run(self.__turn_off_command, shell=True)
            self.__is_on = False

    def turn_on(self) -> None:
        print(qualified_method_name(self.turn_on))
        if not self.__is_on:
            subprocess.run(self.__turn_on_command, shell=True)
            self.__is_on = True

    @staticmethod
    def cec() -> 'Monitor':
        return Monitor('echo \'standby 0\' | cec-client -s -d 1', 'echo \'on 0\' | cec-client -s -d 1')

    @staticmethod
    def video_core() -> 'Monitor':
        return Monitor('vcgencmd display_power 0', 'vcgencmd display_power 1')


# Initialize objects.

pins = GpioPins()
monitor = Monitor.video_core()


# Register a signal handler to clean things up.

def signal_handler(signal, frame) -> None:
    pins.cleanup()
    monitor.turn_off()
    sys.exit()


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


# Watch for motion and turn on the screen when it is detected, so long as it's during daytime hours.

daytime_hours_begin = 6
daytime_hours_end = 22
# daytime_hours_begin = 0
# daytime_hours_end = 24

motionless_timeout_seconds = 60

try:
    monitor.turn_on()
    monitor_turn_off_timestamp = time.time() + motionless_timeout_seconds

    while True:
        is_motion_detected = pins.read_motion_detector()
        pins.write_motion_indicator(is_motion_detected)

        timestamp = time.time()
        hour = time.localtime(timestamp).tm_hour

        if is_motion_detected and hour >= daytime_hours_begin and hour < daytime_hours_end:
            monitor.turn_on()
            monitor_turn_off_timestamp = timestamp + motionless_timeout_seconds
        elif timestamp >= monitor_turn_off_timestamp:
            monitor.turn_off()

        time.sleep(0.2)

finally:
    pins.cleanup()
    monitor.turn_off()
