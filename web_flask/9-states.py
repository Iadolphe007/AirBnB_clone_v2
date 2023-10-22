#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_states():
    """view that lists all of the states"""
    id = None
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, id=id)


@app.route('/states/<id>', strict_slashes=False)
def list_state_cities(id=None):
    """view that lists all cities by their states"""
    found = False
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            found = True
            states = [state]
    if found is False:
        states = []
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def tear_down(error):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
