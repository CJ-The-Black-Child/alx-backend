#!/usr/bin/env python3
"""
A flask app with Babel Setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
    """
    Flask Babel configuration representation.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def get_index() -> str:
    """
    The Home page
    """
    return render_template('4-index.html')


@babel.locale_selector
def get_locale():
    """
    This retrieves a locale from the webpage
    """
    locale = request.args.get('locale')
    if locale and locale in app.config('LANGUAGES'):
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if '__name__' == '__main__':
    app.run(host='0.0.0.0', port=5000)
