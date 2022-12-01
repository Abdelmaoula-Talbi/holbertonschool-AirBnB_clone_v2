#!/usr/bin/python3
"""
A module that representes a script that  starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """function to return the message to display in the user's browser"""
    return "<p>Hello HBNB!</p>"
@app.run(host=0.0.0.0)
