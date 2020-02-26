import json
from http.server import HTTPServer, SimpleHTTPRequestHandler

from interdaktive.config import Config
from interdaktive.state_machine import StateMachine


class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == '/config':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(vars(self.server.config)))
            return

        super().do_GET()


class Server(HTTPServer):
    config: Config
    state_machine: StateMachine

    def __init__(self, config: Config, state_machine: StateMachine):
        super().__init__(('', config.server_port), RequestHandler)
        self.config = config
        self.state_machine = state_machine
