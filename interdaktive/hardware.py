from enum import Enum
from typing import Any, Callable, Optional, Tuple

from gpiozero import LED, Button, MotionSensor

from interdaktive.config import Config
from interdaktive.display import Display


class BlinkRate(Enum):
    SLOW = 1.5
    FAST = 0.33


def optional_led_blink(led: Optional[LED], rate: BlinkRate) -> None:
    if led is not None:
        led.blink(rate.value, rate.value, background=True)


def optional_led_off(led: Optional[LED]) -> None:
    if led is not None:
        led.off()


def optional_led_on(led: Optional[LED]) -> None:
    if led is not None:
        led.on()


class Hardware(object):
    control_button: Optional[Button]
    display: Display
    motion_led: Optional[LED]
    motion_sensor: MotionSensor
    running_led: Optional[LED]

    def __init__(self, config: Config):
        self.display = Display.create(config.display_type)
        self.motion_sensor = MotionSensor(config.motion_sensor_pin)

        if config.control_button_pin is not None:
            self.control_button = Button(config.control_button_pin, hold_time=5)

        if config.motion_led_pin is not None:
            self.motion_led = LED(config.motion_led_pin)

        if config.running_led_pin is not None:
            self.running_led = LED(config.running_led_pin)

    def display_off(self, *args: Any, **kwargs: Any) -> 'Hardware':
        self.display.off()
        return self

    def display_on(self, *args: Any, **kwargs: Any) -> 'Hardware':
        self.display.on()
        return self

    def motion_led_blink(self, rate: BlinkRate, *args: Any, **kwargs: Any) -> 'Hardware':
        optional_led_blink(self.motion_led, rate)
        return self

    def motion_led_off(self, *args: Any, **kwargs: Any) -> 'Hardware':
        optional_led_off(self.motion_led)
        return self

    def motion_led_on(self, *args: Any, **kwargs: Any) -> 'Hardware':
        optional_led_on(self.motion_led)
        return self

    def running_led_off(self, *args: Any, **kwargs: Any) -> 'Hardware':
        optional_led_off(self.running_led)
        return self

    def running_led_on(self, *args: Any, **kwargs: Any) -> 'Hardware':
        optional_led_on(self.running_led)
        return self
