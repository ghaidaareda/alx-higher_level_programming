#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url, method='GET')
    with urllib.request.urlopen(req) as response:
        content = response.read()
        try:
            print(content)
        except urllib.error.URLError as e:
            print("Error code:", e.responses)
