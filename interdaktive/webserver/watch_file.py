import os
import signal
import sys
from typing import Any, Callable, Dict, Optional, Tuple

from watchdog.events import (FileSystemEvent, LoggingEventHandler,
                             PatternMatchingEventHandler)
from watchdog.observers import Observer

WatchFileCallback = Callable[[str], None]


class FileCallbackEventHandler(PatternMatchingEventHandler):
    __abs_file_path: str
    __callback: WatchFileCallback

    def __init__(self, abs_file_path: str, callback: WatchFileCallback):
        super().__init__(patterns=[abs_file_path], ignore_directories=True)
        self.__abs_file_path = abs_file_path
        self.__callback = callback

    def on_any_event(self, event: FileSystemEvent) -> None:
        self.__callback(self.__abs_file_path)


def watch_file(file_path: str, callback: WatchFileCallback) -> None:
    abs_file_path = os.path.abspath(file_path)
    dir_path = os.path.dirname(abs_file_path)

    start_observer = False
    if watch_file.observer is None:
        watch_file.observer = Observer()
        start_observer = True

    event_handler = FileCallbackEventHandler(abs_file_path, callback)
    watch_file.observer.schedule(event_handler, dir_path)

    if start_observer:
        watch_file.observer.start()


watch_file.observer: Optional[Observer] = None


if __name__ == '__main__':
    def callback(abs_file_path) -> None:
        print(abs_file_path)

    for file_path in sys.argv[1:]:
        watch_file(file_path, callback)

    signal.pause()
