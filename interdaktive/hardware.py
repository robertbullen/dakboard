from typing import Optional

from gpiozero import LED, Button, MotionSensor

from interdaktive.config import Config
from interdaktive.display import Display


class Hardware(object):
    control_button: Optional[Button]
    display: Display
    motion_led: Optional[LED]
    motion_sensor: MotionSensor
    running_led: Optional[LED]

    def __init__(config: Config):
        if config.control_button_pin is not None:
            self.control_button = Button(config.control_button_pin)
        self.display = Display(config.display_type)
