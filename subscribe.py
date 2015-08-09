"""
Subscrbe to an Instagram tag
"""
import os
import sys
import urllib
import urllib2
from requests2 import Request2

if __name__ == '__main__':
    URL = "https://api.instagram.com/v1/subscriptions/"
    CALLBACK = os.environ.get("INSTAGRAM_CALLBACK")
    CLIENT_ID = os.environ.get("INSTAGRAM_CLIENT_ID")
    CLIENT_SECRET = os.environ.get("INSTAGRAM_CLIENT_SECRET")

    try:
        tag = sys.argv[1]
    except:
        raise Exception("Missing tag! Format should be 'python subscribe.py <tag>'")

    FULL_CALLBACK = "%(callback)s/%(tag)s" % {
        "callback": CALLBACK,
        "tag": tag
    }

    print "Callback: %s" % CALLBACK
    print "Client ID: %s" % CLIENT_ID
    print "Client Secret: %s\n" % CLIENT_SECRET

    print "Full Callback: %s\n" % FULL_CALLBACK

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    body = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "object": "tag",
        "aspect": "media",
        "callback_url": FULL_CALLBACK,
        "object_id": tag
    }

    encoded_body = urllib.urlencode(body)
    print "Encoded Body: %s" % encoded_body

    # Build HTTP Request
    req = Request2(URL, method="POST", data=encoded_body, headers=headers)

    try:
        response = urllib2.urlopen(req)
        code = response.getcode()
        print "\nResponse: %s\n" % response.read()
    except urllib2.HTTPError, e:
        print "\nERROR! Code: %s, Desc: %s\n" % (str(e.code), e.read())
    except Exception:
        raise
