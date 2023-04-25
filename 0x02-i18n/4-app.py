#!/usr/bin/env python3
"""
This module implements a Flask application with localization support
using Flask-Babel.
"""

from typing import Tuple

from flask import Flask, render_template, request
from flask_babel import Babel
from flask_babel import _


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    supported_locales = app.config['LANGUAGES']
    locale = request.args.get('locale')
    if locale in supported_locales:
        return locale
    return request.accept_languages.best_match(supported_locales)


@app.route('/')
def index() -> Tuple[str, int]:
    title = _('home_title')
    header = _('home_header')
    return render_template('4-index.html', title=title,
                           header=header)


if __name__ == "__main__":
    app.run(host='localhost', debug=True)
