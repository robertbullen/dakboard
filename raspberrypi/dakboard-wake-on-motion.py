import RPi.GPIO as gpio
import signal
import time
import subprocess
import sys


# Declare and instantiate a class responsible for the GPIO pins.

class GpioPins:
    motion_detector = 11
    motion_indicator_led = 3
    power_indicator_led = 5

    def __init__(self):
        print('initializing gpio')
        gpio.setwarnings(True)
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.motion_detector, gpio.IN)
        gpio.setup(self.motion_indicator_led, gpio.OUT, initial=gpio.LOW)
        gpio.setup(self.power_indicator_led, gpio.OUT, initial=gpio.HIGH)

    def cleanup(self) -> None:
        print('cleaning up gpio')
        gpio.cleanup()

    def read_motion_detector(self) -> bool:
        is_motion_detected = bool(gpio.input(self.motion_detector))
        print('read_motion_detector', is_motion_detected)
        return is_motion_detected

    def write_motion_indicator(self, is_motion_detected: bool) -> None:
        print('write_motion_indicator', is_motion_detected)
        gpio.output(self.motion_indicator_led, is_motion_detected)


pins = GpioPins()


# Declare and instantiate a class responsible for turning on/off the monitor.

class Monitor:
    is_on = False

    def turn_on(self) -> None:
        if not self.is_on:
            subprocess.run('echo \'on 0\' | cec-client -s -d 1', shell=True)
            self.is_on = True

    def turn_off(self) -> None:
        if self.is_on:
            subprocess.run('echo \'standby 0\' | cec-client -s -d 1', shell=True)
            self.is_on = False


monitor = Monitor()


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
