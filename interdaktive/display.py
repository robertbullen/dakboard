import logging
import subprocess
from typing import Any, Callable, Optional


# Declare and instantiate a class responsible for turning on/off the display.
class Display:
    __is_on: Optional[bool]
    __off: Callable[[], Any]
    __on: Callable[[], Any]
    __type: str

    def __init__(self, type: str, off: Callable[[], Any], on: Callable[[], Any]) -> None:
        self.__is_on = None
        self.__off = off  # type: ignore
        self.__on = on  # type: ignore
        self.__type = type

    def __repr__(self) -> str:
        return "Display(type='{0}', is_on={1})".format(self.__type, self.__is_on)

    def __str__(self) -> str:
        return self.__type

    @property
    def is_on(self) -> Optional[bool]:
        return self.__is_on

    def off(self) -> None:
        if self.__is_on != False:
            self.__off()  # type: ignore
            self.__is_on = False

    def on(self) -> None:
        if self.__is_on != True:
            self.__on()  # type: ignore
            self.__is_on = True

    def toggle(self) -> None:
        if self.__is_on == None or self.__is_on == True:
            self.off()
        else:
            self.on()

    @staticmethod
    def create(arg: str) -> 'Display':
        if arg == 'cec':
            return Display.cec()
        if arg == 'mock':
            return Display.mock()
        if arg == 'video-core':
            return Display.video_core()
        raise ValueError(arg)

    @staticmethod
    def cec() -> 'Display':
        return Display(
            type='cec',
            off=lambda: subprocess.run("echo 'standby 0' | cec-client -s -d 1", shell=True),
            on=lambda: subprocess.run("echo 'on 0' | cec-client -s -d 1", shell=True),
        )

    @staticmethod
    def mock() -> 'Display':
        logger = logging.getLogger(__name__)
        return Display(
            type='mock',
            off=lambda: logger.info('Turning off mock display'),
            on=lambda: logger.info('Turning on mock display'),
        )

    @staticmethod
    def video_core() -> 'Display':
        return Display(
            type='video-core',
            off=lambda: subprocess.run('vcgencmd display_power 0', shell=True),
            on=lambda: subprocess.run('vcgencmd display_power 1', shell=True),
        )
