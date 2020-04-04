from functools import partial
from typing import Any, Callable, Optional

from gpiozero import LED, Button, MotionSensor

from interdaktive.config import Config
from interdaktive.display import Display


def optional_led_blink(led: Optional[LED], *args: Any, **kwargs: Any) -> None:
    if led is not None:
        led.blink(0.5, 0.5, background=True)


def optional_led_off(led: Optional[LED], *args: Any, **kwargs: Any) -> None:
    if led is not None:
        led.off()


def optional_led_on(led: Optional[LED], *args: Any, **kwargs: Any) -> None:
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

        self.motion_led_blink = partial(optional_led_blink, self.motion_led)  # type: ignore
        self.motion_led_off = partial(optional_led_off, self.motion_led)  # type: ignore
        self.motion_led_on = partial(optional_led_on, self.motion_led)  # type: ignore

        self.running_led_off = partial(optional_led_off, self.running_led)  # type: ignore
        self.running_led_on = partial(optional_led_on, self.running_led)  # type: ignore

    def display_off(self, *args: Any, **kwargs: Any) -> None:
        self.display.off()

    def display_on(self, *args: Any, **kwargs: Any) -> None:
        self.display.on()

    motion_led_blink: Callable[..., None]
    motion_led_off: Callable[..., None]
    motion_led_on: Callable[..., None]

    running_led_off: Callable[..., None]
    running_led_on: Callable[..., None]
