#!/usr/bin/python3
"""
A module that representes a script that  starts a Flask web application
"""

from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display the message on the /number page"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """function to diplay the message on the (number_template page"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def num_odd_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
