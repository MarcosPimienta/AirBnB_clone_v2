#!/usr/bin/python3
"""Flask """
from flask import Flask


app = Flask(__name__)


""" @app.route('/', strict_slashes=False)
@app.route('/hbnb', strict_slashes=False)
@app.route('/c/<text>', strict_slashes=False) """

@app.route('/python/<text>', strict_slashes=False)
def hello_world(text="is cool"):
    return 'Python {}'.format(text).replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
