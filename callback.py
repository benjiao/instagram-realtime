"""
A simple flask app for handling callbacks that the instagram
service should call.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/<tag>')
def index(tag):
    print tag

    return tag

app.run(host='0.0.0.0', debug=True)
