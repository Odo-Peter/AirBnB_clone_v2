#!/usr/bin/python3
"""
Python script that starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    returns a str - 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returns 'HBNB'
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def Ctext(text):
    """
    returns a text
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def pythonfun(text='is cool'):
    """[summary of args]
    Args:
    text ([type]): [description]
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run('0.0.0.0', port='5000')
