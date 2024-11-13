#!/usr/bin/env python3
"""
    flask app that render a template
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """
        root view to render a root template
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
