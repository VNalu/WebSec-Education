# Entry point for the application.
# from . import app    # For application discovery by the 'flask' command. 
from views import views  # For import side-effects of setting up routes. 
from flask import Flask
from flask_socketio import SocketIO

# Time-saver: output a URL to the VS Code terminal so you can easily Ctrl+click to open a browser
# print('http://127.0.0.1:5000/hello/VSCode')

app = Flask(__name__)
app.register_blueprint(views)
app.secret_key = "aintreallyasecret" 
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0")