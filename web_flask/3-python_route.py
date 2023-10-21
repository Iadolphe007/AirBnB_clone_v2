#!/usr/bin/python3
"""script that start flask application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """display"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """dsiplay"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_txt(text):
    """display c ..."""
    text = text.replace('_', ' ')
    return ("C {}".format(text))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello_pyt(text="is cool"):
    """display python ..."""
    txt = text.replace("_", " ")
    return ("python {}".format(txt))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
