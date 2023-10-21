#!/usr/bin/python3
"""script that strat web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
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


@app.route('/python',  defaults={'text': "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello_pyt(text):
    """display python ..."""
    txt = text.replace("_", " ")
    return ("python {}".format(txt))


@app.route('/number/<int:n>/', strict_slashes=False)
def number(n):
    """display number"""
    if isinstance(n, int):
        return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display template"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    if isinstance(n, int):
        if n % 2 == 0:
            num = 'even'
        else:
            num = 'odd'
        return render_template("6-number_odd_or_even.html", n=n, num=num)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
