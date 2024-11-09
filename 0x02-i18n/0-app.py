#!/usr/bin/env python3
"""
    flask app that render a template
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home() -> str:
    """
        root view to render a root template
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
