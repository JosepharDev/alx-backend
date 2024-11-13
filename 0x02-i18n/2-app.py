#!/usr/bin/env python3
"""
    flask app that render a template
"""
from flask import Flask
from flask import request
from flask_babel import Babel
from flask import render_template


class Config:
    """Config Class"""
    LANGUAGE = ['en', 'fr']
    BABEL_DEFAULT_LOCAL = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.

    Returns:
        str: best match
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
        root view to render a root template
    """
    return render_template('2-index.html',)


if __name__ == '__main__':
    app.run()
