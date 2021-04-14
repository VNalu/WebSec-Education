from flask import Flask
from multiprocessing.connection import Client
import time

app = Flask(__name__)

# Create connection to websec app
address = ("web", 5001)
connection = Client(address, authkey=b"aliens-are-already-here")
connection.send("test") # DEBUG: Test message (remove later)