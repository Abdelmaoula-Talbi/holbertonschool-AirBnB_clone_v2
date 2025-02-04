#!/usr/bin/python3
"""
A module that representes a script that  starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """function to return the message to display in the user's browser"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """function to return the message to display on the /hbnb page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """function to display the message on the /c page"""
    return "C" + " " + text.replace("_", " ")


@app.route("/python")
@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """function to display message on the /python page"""
    return "Python" + " " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
