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
    """function"""
    return "C" + " " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
