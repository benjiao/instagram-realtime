"""
An extension of the urllib2 Request object that allows user to specify
the request method.

This is to allow sending of HTTPS requests using types like DELETE, PATCH, etc.
"""

import urllib2


class Request2(urllib2.Request):
    def __init__(self, url, method, data=None, headers={}):
        self._method = method
        urllib2.Request.__init__(self, url=url, headers=headers, data=data)

    def get_method(self):
        if self._method:
            return self._method
        else:
            return urllib2.Request.get_method(self)
