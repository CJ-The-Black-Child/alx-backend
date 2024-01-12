#!/usr/bin/env python3
"""
A flask app with babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    Flask Babel configuration representation
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)  # instantiate the babel object


@app.route('/')
def get_index() -> str:
    """
    This is the get request for the homepage
    """
    return render_template('1-index.html')


if '__name__' == '__main__':
    app.run(host='0.0.0.0', port=5000)
