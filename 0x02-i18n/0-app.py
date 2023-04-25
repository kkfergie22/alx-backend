#!/usr/bin/env python3
"""Basic flask app for initial translation"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    This function is the view function for the root route of the Flask app.
    It renders an HTML template named '0-index.html'
    and returns it as a string.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='localhost', debug=True)
