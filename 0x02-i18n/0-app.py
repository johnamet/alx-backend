#!/usr/bin/env python3
from flask import Flask, render_template
from flask_babel import Babel, _

"""
The module contains a flask application factory,
as explained here:
http://flask.pocoo.org/docs/patterns/appfactories/

"""


class Config:
    """
    The configuration class holds all of
    the application factorie's configuration   '
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    The home page
    :return:
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
