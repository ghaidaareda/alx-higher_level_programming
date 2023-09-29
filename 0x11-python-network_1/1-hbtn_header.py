#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url, method='GET')
    with urllib.request.urlopen(req) as response:
        content = response.read()
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
