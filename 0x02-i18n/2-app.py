#!/usr/bin/env python3
"""
This module implements a Flask application with localization support
using Flask-Babel.

The application uses the Babel extension to support internationalization (i18n)
and localization (l10n) of the content displayed in the templates.
It allows the user to select their preferred language
through the Accept-Language HTTP header or a query parameter in the URL.
The application is configured to support two languages: English and French.
"""

from typing import Tuple

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    This class defines the configuration parameters for the Flask application.

    Attributes:
        LANGUAGES (list): A list of available languages supported
        by the application.
        DEFAULT_LOCALE (str): The default locale for the application.
        DEFAULT_TIMEZONE (str): The default timezone for the application.
    """
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCALE = 'en'
    DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale() -> str:
    """
    This function determines the user's preferred locale for the application.

    It tries to find the best match between the available languages and
    the user's preferences,either through the Accept-Language HTTP header
    or a query parameter in the URL.

    Returns:
        The preferred locale for the application as a string.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.config.from_object(Config)


@app.route('/')
def index() -> Tuple[str, int]:
    """
    This function displays the index page of the application.

    It renders the '1-index.html' template using the
    default language specified in the application configuration.

    Returns:
        A tuple containing the rendered HTML template and a status code 200 OK.
    """
    return render_template('1-index.html'), 200


if __name__ == "__main__":
    app.run(host='localhost', debug=True)
