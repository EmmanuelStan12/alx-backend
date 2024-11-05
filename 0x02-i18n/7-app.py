#!/usr/bin/env python3
"""Basic Flask app with i18n support
"""
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union


class Config:
    """Represents babel config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


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


def get_user() -> Union[Dict, None]:
    """Gets the user with the specified id.
    """
    user_id = request.args.get('login_as')
    if user_id:
        try:
            login_id = int(user_id)
            if login_id in users.keys():
                return users[login_id]
        except ValueError:
            return None

    return None

@app.before_request
def before_request() -> None:
    """Executes before every func
    """
    user = get_user()
    g.user = user

@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for the request
    """
    locale = request.args.get('locale')
    if locale:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    locale = request.headers.get('locale', '')
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """Retrieves timezone for request.
    """
    timezone = request.args.get('timezone', '')
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']

@app.route("/")
def index() -> str:
    """Returns a page
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
