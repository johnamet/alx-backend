#!/usr/bin/env python3
"""
The module contains the flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    return (request
            .accept_languages
            .best_match(app.config['LANGUAGES']))


@app.route('/')
def index() -> str:
    """
    The entry point
    :return:
    """
    return render_template('3-index.html',
                           home_title=_('Welcome to Holberton'),
                           home_header=_('Hello world'))


if __name__ == '__main__':
    app.run()
