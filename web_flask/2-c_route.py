#!/usr/bin/python3
"""A script that starts a Flask web application
with variable """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_variable(text):
    format_text = text.replace('_', ' ')
    return f"C {format_text}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
