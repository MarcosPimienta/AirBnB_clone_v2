#!/usr/bin/python3
"""Flask """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
@app.route('/number/<int:n>', strict_slashes=False)
@app.route('/number_template/<int:n>', strict_slashes=False)
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def hello_world(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
