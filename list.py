"""
List all Instagram Subscriptions
"""
import os
import urllib2
from requests2 import Request2

if __name__ == '__main__':
    CALLBACK = os.environ.get("INSTAGRAM_CALLBACK")
    CLIENT_ID = os.environ.get("INSTAGRAM_CLIENT_ID")
    CLIENT_SECRET = os.environ.get("INSTAGRAM_CLIENT_SECRET")

    print "Callback: %s" % CALLBACK
    print "Client ID: %s" % CLIENT_ID
    print "Client Secret: %s\n" % CLIENT_SECRET

    URL = "https://api.instagram.com/v1/subscriptions?client_secret=%(client_secret)s&client_id=%(client_id)s" %\
          {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}

    print "URL: %s\n" % URL

    # Build HTTP Request
    req = Request2(URL, method="GET")

    response = urllib2.urlopen(req)
    code = response.getcode()
    print "Response: %s\n" % response.read()
