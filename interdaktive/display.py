import subprocess
from typing import Optional


# Declare and instantiate a class responsible for turning on/off the display.
class Display:
    __is_on: Optional[bool]
    __off_command: str
    __on_command: str
    __type: str

    def __init__(self, type: str, off_command: str, on_command: str) -> None:
        self.__is_on = None
        self.__off_command = off_command
        self.__on_command = on_command
        self.__type = type

    def __repr__(self) -> str:
        return "Display(type='{0}', is_on={3}, off_command=\"{1}\", on_command=\"{2}\")".format(
            self.__type,
            self.__is_on,
            self.__off_command,
            self.__on_command,
        )

    def __str__(self) -> str:
        return self.__type

    @property
    def is_on(self) -> Optional[bool]:
        return self.__is_on

    def off(self) -> None:
        if self.__is_on != False:
            subprocess.run(self.__off_command, shell=True)
            self.__is_on = False

    def on(self) -> None:
        if self.__is_on != True:
            subprocess.run(self.__on_command, shell=True)
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
            off_command="echo 'standby 0' | cec-client -s -d 1",
            on_command="echo 'on 0' | cec-client -s -d 1",
        )

    @staticmethod
    def mock() -> 'Display':
        return Display(
            type='mock',
            off_command="echo 'display off'",
            on_command="echo 'display on'",
        )

    @staticmethod
    def video_core() -> 'Display':
        return Display(
            type='video-core',
            off_command='vcgencmd display_power 0',
            on_command='vcgencmd display_power 1',
        )
