from datetime import datetime
from flask import Flask, render_template
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

@app.route("/cross-site-scripting")
def cross_site_scripting():
    return render_template("todo.html") # Change to cross-site-scripting when made
