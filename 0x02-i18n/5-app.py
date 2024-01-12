#!/usr/bin/env python3
"""
A flask app with Babel config
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Union, Dict


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
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    This retrieves user based ids
    """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """
    Executes routines before each request resolution
    """
    g.user = get_user()


@app.route('/')
def index():
    """
    Home Page
    """
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    This retrieves a locale from the webpage
    """
    if g.user:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
