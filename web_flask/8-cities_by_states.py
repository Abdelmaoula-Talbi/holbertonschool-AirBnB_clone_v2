#!/usr/bin/python3
"""A module that representes a script that  starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_of_state():
    """function to display the html page of list of cities of one state"""
    states = storage.all(State).values()
    state_cities = []
    for state in states:
        for city in state.cities:
            state_cities.append(city)
    return render_template("8-cities_by_states.html",
                           states=states, state_cities=state_cities)


@app.teardown_appcontext
def remove_session(exception):
    """ remove the current SQLAlchemy Session:"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
