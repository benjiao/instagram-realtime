"""
A simple flask app for handling callbacks that the instagram
service should call.
"""

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/<tag>')
def index(tag):
    print "Tag: %s" % tag
    print "Request Data: %s" % request.data

    challenge = request.args.get('hub.challenge')
    print "Challenge: %s" % challenge
    if challenge is not None:
        return challenge

    return tag

app.run(host='0.0.0.0', debug=True)
