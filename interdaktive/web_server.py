import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from io import BytesIO
from typing import Dict, List, cast
from urllib.parse import parse_qs, urlparse

from interdaktive.config import Config, format_time
from interdaktive.state_machine import StateMachine


class WebRequestHandler(SimpleHTTPRequestHandler):
    pass


class WebServer(HTTPServer):
    config: Config
    state_machine: StateMachine

    def __init__(self, config: Config, state_machine: StateMachine):
        super().__init__(('', config.web_server_port), WebRequestHandler)
        self.config = config
        self.state_machine = state_machine


class WebRequestHandler(SimpleHTTPRequestHandler):  # type: ignore # Name 'WebRequestHandler' already defined on line...
    @property
    def web_server(self) -> WebServer:
        return cast(WebServer, self.server)

    def do_GET(self) -> None:
        url = urlparse(self.path)

        if url.path == '/config':
            config_dict = vars(self.web_server.config)
            config_dict['waking_hours_begin'] = format_time(self.web_server.config.waking_hours_begin)
            config_dict['waking_hours_end'] = format_time(self.web_server.config.waking_hours_end)
            body = json.dumps(config_dict).encode('utf-8')

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(body)

            return

        if url.path == '/state-diagram':
            machine = self.web_server.state_machine.machine
            machine.machine_attributes['labelloc'] = 'top'

            query_params: Dict[str, List[str]] = parse_qs(url.query)
            prog_list: List[str] = query_params.get('prog', ['dot'])
            prog: str = prog_list.pop()

            if prog == 'circo':
                machine.machine_attributes['ratio'] = '0.75'
            else:
                machine.machine_attributes['ratio'] = '0.33'
            graph = machine.get_graph(force_new=True)

            image = BytesIO()
            graph.draw(image, format='png', prog=prog)
            body = image.getvalue()
            image.close()

            self.send_response(200)
            self.send_header('Content-Type', 'image/png')
            self.end_headers()
            self.wfile.write(body)

            return

        super().do_GET()
