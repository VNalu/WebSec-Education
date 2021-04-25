from datetime import datetime
from flask import Flask, render_template, url_for, request
from . import app

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
    return render_template("labs/xss1.html")

@app.route('/api/v1/request/new', methods=['POST'])
def new_request():
    data = request.get_json() # TODO: Parse json
    if not validate_session(data["session_id"]):
        return {"status": "error", "error": "invalid session id"}
    
    # TODO: Add request to user queue
    return {"status": "success"}

# TODO: Make UI for request
# TODO: Figure out forward editted request for proxy 
