#!/usr/bin/python3
"""
python script that kicks off a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Returns a simple 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returns a string - 'HBNB'
    """
    return "HBNB"


if __name__ == '__main__':
    app.run('0.0.0.0', port='5000')
