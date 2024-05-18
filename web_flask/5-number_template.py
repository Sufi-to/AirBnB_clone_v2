#!/usr/bin/python3
"""Script that starts a Flask web application, templates will be used."""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_hbnb_route(text):
    up_text = ""
    if "_" in text:
        up_text = "C "
        for i in text:
            if i == "_":
                up_text += " "
            else:
                up_text += i
    else:
        return f"C {text}"
    return up_text


@app.route("/python/", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_cool(text):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def number_template(n):
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
