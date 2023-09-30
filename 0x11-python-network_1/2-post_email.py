#!/usr/bin/python3
"""
script that takes in a URL & email,
sends a POST request to the URL with email
and displays the  body of the response (decoded in utf-8)
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    mail = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(mail)
    data = data.encode('ascii')
    req = urllib.request.Request(url ,data)
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf8')
        print(content)
