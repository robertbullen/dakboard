import argparse
from typing import Optional


class Config(argparse.Namespace):
    log_file_path: Optional[str]
    port: int
    refresh_seconds: int
    state_diagram_file_path: Optional[str]

    @staticmethod
    def from_args() -> 'Config':
        parser = argparse.ArgumentParser(prog='python3 -m interdaktive.webserver')

        parser.add_argument(
            '--log-file-path',
            help='The file path from which to serve logging output.',
        )

        parser.add_argument(
            '--port',
            default=5000,
            help='The port to which the webserver will bind.'
        )

        parser.add_argument(
            '--refresh-seconds',
            default=3,
            help='The interval in seconds that the browser will request updated content.'
        )

        parser.add_argument(
            '--state-diagram-file-path',
            help='The file path from which to state diagram images.',
        )

        return parser.parse_args(namespace=Config())
