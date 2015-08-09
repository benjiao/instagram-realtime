"""
A simple flask app for handling callbacks that the instagram
service should call.
"""

import logging
from flask import Flask
from flask import request
from flask import make_response

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.DEBUG)
app = Flask(__name__)


@app.route('/<tag>/', methods=["GET"])
def index(tag):
    logging.info("Tag: %s" % tag)
    logging.info("Request Data: %s" % request.data)

    challenge = request.args.get('hub.challenge')
    logging.info("Challenge: %s", challenge)
    if challenge is not None:
        return challenge
    else:
        return make_response("OK", 400)


@app.route('/<tag>/', methods=["POST"])
def receive(tag):
    logging.info("Tag: %s" % tag)
    logging.info("Request Data: %s" % request.data)

    return make_response("OK", 200)

app.run(host='0.0.0.0', debug=True)
