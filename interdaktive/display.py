import subprocess
import typing


# Declare and instantiate a class responsible for turning on/off the display.
class Display:
    __is_on: typing.Union[bool, None]
    __off_command: str
    __on_command: str

    def __init__(self, off_command: str, on_command: str):
        self.__is_on = None
        self.__off_command = off_command
        self.__on_command = on_command

    @property
    def is_on(self) -> typing.Union[bool, None]:
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


cec = Display(
    off_command="echo 'standby 0' | cec-client -s -d 1",
    on_command="echo 'on 0' | cec-client -s -d 1"
)

mock = Display(
    off_command="echo 'display off'",
    on_command="echo 'display on'"
)

video_core = Display(
    off_command='vcgencmd display_power 0',
    on_command='vcgencmd display_power 1'
)
