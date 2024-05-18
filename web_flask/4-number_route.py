#!/usr/bin/python3
"""Script that starts a Flask web application route of python is cool."""

from flask import Flask

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
	return f"{n} is a Number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
