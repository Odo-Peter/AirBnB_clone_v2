#!/usr/bin/python3
"""
python script that starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Returns a 'Hello HBNB!' string
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run('0.0.0.0', port='5000')
