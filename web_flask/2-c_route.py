#!/usr/bin/python3
"""Script that starts a Flask web application and more routes and more."""

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
    print(text)
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
