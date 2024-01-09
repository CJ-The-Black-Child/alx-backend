#!/usr/bin/env python3
"""
A flask app with Babel config
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config(object):
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)


babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    g.user = get_user()


@app.route('/')
def index():
    """
    Home Page
    """
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """
    Locale from URL parameters
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    """
    Locale from user settings
    """
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    """
    Locale from request header
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
