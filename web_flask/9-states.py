#!/usr/bin/python3
"""A module that representes a script that  starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def all_states():
    """function to display the html page of list of states"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def cities_by_stateid(id):
    """function to display html page of list of cities based on the state id"""
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template("9-states.html", state=state,
                                   state_cities=state.cities)
        else:
            return render_template("9-states.html", id_not_found=True)


@app.teardown_appcontext
def remove_session(exception):
    """ remove the current SQLAlchemy Session:"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
