import logging

from flask import Flask, render_template, send_file
from flask_socketio import SocketIO, emit

from interdaktive.webserver.config import Config
from interdaktive.webserver.watch_file import watch_file

if __name__ == '__main__':
    config = Config.from_args()

    app = Flask(__name__)

    # This app must specify `async_mode='threading'` when constructing the _SocketIO_ instance for
    # it to play nicely with _watchdog_. Here's why:
    #
    # _SocketIO_ prefers `async_mode='eventlet'` over `async_mode='threading'` for good reasons:
    #   - Using _eventlet_ scales better than _threading_.
    #   - Using _eventlet_ enables true websocket support whereas using _threading_ falls back to
    #     client-side long-polling.
    #
    # Meanwhile _watchdog_ supports only _threading_ for its async operations. If attempts are made
    # to invoke _SocketIO_ send/emit functions from a _threading_ thread, _SocketIO_ will silently
    # fail to deliver those messages due to the mixed async metaphors.
    #
    # A few workarounds are possible:
    #   - Separate the _SocketIO_ and _watchdog_ responsibilities into individual processes that
    #     leverage their prefered async mechanism and then build an IPC bridge between them. This
    #     is discussed briefly at https://flask-socketio.readthedocs.io/en/latest/#using-multiple-workers.
    #   - Use _SocketIO_'s `start_background_task()` utility function to transition from _watchdog_
    #     threads to _SocketIO_'s current async model before sending messages.
    #   - Force _SocketIO_ to use _threading_. This results in a loss of the _eventlet_ advantages
    #     listed above, but has the advantage of being the simplest solution and also makes this
    #     app lighter weight in that _eventlet_ is one less dependency that must be installed.
    #
    # Ultimately, this is a very low-scale, low-tech app, so the last workaround was chosen as the
    # quickest and easiest way to get things working reliably.
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

    socketio.run(app, debug=config.debug, host='0.0.0.0', port=config.port, ssl_context='adhoc')
