#!/usr/bin/env python3
"""
    flask app that render a template
"""
from flask import Flask
from flask_babel import Babel
from flask import render_template


class Config:
    """Config Class"""
    LANGUAGE = ['en', 'fr']
    BABEL_DEFAULT_LOCAL = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
bable = Babel(app)


@app.route('/')
def home() -> str:
    """
        root view to render a root template
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
