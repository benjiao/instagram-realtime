"""
Clears all user subscriptions to instagram
"""

"""
Subscrbe to an Instagram tag
"""
import os
import sys
import urllib
import urllib2
from requests2 import Request2

if __name__ == '__main__':
    CALLBACK = os.environ.get("INSTAGRAM_CALLBACK")
    CLIENT_ID = os.environ.get("INSTAGRAM_CLIENT_ID")
    CLIENT_SECRET = os.environ.get("INSTAGRAM_CLIENT_SECRET")

    print "Client ID: %s" % CLIENT_ID
    print "Client Secret: %s\n" % CLIENT_SECRET

    URL = ("https://api.instagram.com/v1/subscriptions/?client_secret=%(client_secret)s" +
           "&object=all&client_id=%(client_id)s") % {"client_secret": CLIENT_SECRET,
                                                     "client_id": CLIENT_ID}

    print "URL: %s\n" % URL

    # Build HTTP Request
    req = Request2(URL, method="DELETE")

    try:
        response = urllib2.urlopen(req)
        code = response.getcode()
        print "\nResponse: %s\n" % response.read()
    except urllib2.HTTPError, e:
        print "\nERROR! Code: %s, Desc: %s\n" % (str(e.code), e.read())
    except Exception:
        raise
