import logging

from flask import Flask, render_template, send_file

from interdaktive.webserver.config import Config

if __name__ == '__main__':
    config = Config.from_args()

    app = Flask(__name__)

    @app.route('/')
    def index():  # type: ignore
        return render_template('index.html', refreshSeconds=config.refresh_seconds)

    if config.state_diagram_file_path is not None:
        @app.route('/content/state-diagram')
        def state_diagram():  # type: ignore
            return send_file(config.state_diagram_file_path)

    if config.log_file_path is not None:
        @app.route('/content/log')
        def log():  # type: ignore
            return send_file(config.log_file_path)

    app.run(debug=True, host='0.0.0.0', port=config.port)
