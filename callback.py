"""
A simple flask app for handling callbacks that the instagram
service should call.
"""

import logging
from flask import Flask
from flask import request

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.DEBUG)
app = Flask(__name__)


@app.route('/<tag>/')
def index(tag):
    logging.info("Tag: %s" % tag)
    logging.info("Request Data: %s" % request.data)

    challenge = request.args.get('hub.challenge')
    logging.info("Challenge: %s", challenge)
    if challenge is not None:
        return challenge

    return tag

app.run(host='0.0.0.0', debug=True)
