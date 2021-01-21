#!/usr/bin/python3
"""Start a flask app"""
from flask import Flask, render_template
from models import storage
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """display cities"""
    cities = storage.all(City)
    return render_template("8-cities_by_states.html", cities=cities)


@app.teardown_appcontext
def close_storage(exception):
    """remove the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
