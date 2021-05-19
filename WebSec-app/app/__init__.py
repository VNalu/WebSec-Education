# Entry point for the application.
from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

# app = Flask(__name__)
# socketio = SocketIO(app)
# app.register_blueprint(views)
# app.secret_key = "aintreallyasecret" 

# if __name__ == '__main__':
#     socketio.run(app, debug=True, host="0.0.0.0")

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = "aintreallyasecret" 

    from .main import viewsBP as views_blueprint
    app.register_blueprint(views_blueprint)

    socketio.init_app(app)
    return app