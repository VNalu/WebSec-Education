from datetime import datetime
from flask import Flask, render_template, url_for, request,flash, jsonify
from . import app
from queue import Queue
import sys

requestsToEditQueue = Queue()

@app.route("/")
def home():
    return render_template("index.html")

# Leaving hello in as an example
@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/lessons/cross-site-scripting-lesson1")
def xss_lesson1():
    return render_template("lessons/xss1.html")

@app.route("/lessons/cross-site-scripting-lab1")
def xss_lab1():
    packet_to_edit = "This is where the packet can be edited."
    cookie_to_edit = "This is where the cookies can be edited."
    return render_template("labs/xss1.html", packet=packet_to_edit, cookies=cookie_to_edit)

@app.route('/api/v1/request/new', methods=['POST'])
def new_request():
    print("Raw: ", request.json, file=sys.stderr)
    data = request.json
    print("Data: ", data, file=sys.stderr)
    requestsToEditQueue.put(data)

    if not validate_session(data["Session ID"]):
        return {"status": "error", "error": "invalid session id"}
    
    # TODO: Add request to user queue
    return {"status": "success"}

# TODO: Write function to put data in data structure callable by javascript
@app.route('/api/v1/request', methods=['GET'])
def get_request():
    if requestsToEditQueue.empty():
        return jsonify({"request": None})
    return jsonify({"request": requestsToEditQueue.get()})

# TODO: Validate session
def validate_session(sess_id):
    if sess_id == "123":
        print("Good session id", file=sys.stderr)
        return True
    print("Bad session id", file=sys.stderr)
    return False