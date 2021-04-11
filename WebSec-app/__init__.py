from flask import Flask
from multiprocessing.connection import Listener

app = Flask(__name__)

# Create connection to proxy
address = ("0.0.0.0", 5001)
listener = Listener(address, authkey=b"aliens-are-already-here")
connection = listener.accept()
