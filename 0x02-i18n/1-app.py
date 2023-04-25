#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCALE = 'en'
    DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='localhost', debug=True)
