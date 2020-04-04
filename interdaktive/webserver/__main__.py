import logging

from flask import Flask, render_template, send_file
from flask_socketio import SocketIO, emit

from interdaktive.webserver.config import Config
from interdaktive.webserver.watch_file import watch_file

if __name__ == '__main__':
    config = Config.from_args()

    app = Flask(__name__)

    # SocketIO prefers an `async_mode` of 'eventlet', but that causes a problem in this app so
    # 'threading' is specified instead.
    #
    # More info: The *watchdog* package is used for watching files, and it does so on a separate
    # 'threading' thread. If that thread attempts to send/emit a websocket message using SocketIO
    # utilizing 'eventlet', that message is never transmitted. So even though 'eventlet' may scale
    # better than 'threading', this is a very low-scale app and setting `async_mode='threading'`
    # was the quickest and easiest solution.
    socketio = SocketIO(app, async_mode='threading')

    @app.route('/')
    def get_index():  # type: ignore
        return render_template('index.html')

    def update_clients(route: str) -> None:
        socketio.emit('update', {'route': route})

    if config.state_diagram_file_path is not None:
        state_diagram_route = '/content/state-diagram'

        @app.route(state_diagram_route)
        def get_state_diagram():  # type: ignore
            return send_file(config.state_diagram_file_path)

        watch_file(
            config.state_diagram_file_path,
            lambda abs_file_path: update_clients(state_diagram_route)
        )

    if config.log_file_path is not None:
        log_route = '/content/log'

        @app.route(log_route)
        def get_log():  # type: ignore
            return send_file(config.log_file_path)

        watch_file(
            config.log_file_path,
            lambda abs_file_path: update_clients(log_route)
        )

    socketio.run(app, debug=config.debug, host='0.0.0.0', port=config.port)
