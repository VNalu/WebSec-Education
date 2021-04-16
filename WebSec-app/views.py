from datetime import datetime
from flask import Flask, render_template, url_for
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