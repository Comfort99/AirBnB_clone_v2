#!/usr/bin/python3
""" A script that start  a Flask web application
using variables and integers """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_variable(text):
    format_text = text.replace('_', ' ')
    return f"C {format_text}"


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def hello_default(text):
    format_tex = text.replace('_', ' ')
    return f"Python {format_tex}"


@app.route('/number/<int:n>', strict_slashes=False)
def Boolean(n):
    return f'{n} is a number'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
