#!/usr/bin/env python3
"""
A flask app with Babel setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def get_index() -> str:
    """
    Get request for the home page
    """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """
    This retrieves a locale from the webpage
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if '__name__' == '__main__':
    app.run(host='0.0.0.0', port=5000)
