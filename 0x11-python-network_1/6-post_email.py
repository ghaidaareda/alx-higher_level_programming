#!/usr/bin/python3
"""
script that takes in a URL & email,
sends a POST request to the URL with email
and displays the  body of the response.
usin requests lib.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    mail = {"email": sys.argv[2]}
    req = Requests.post(url, data=mail)
    print(req.text)
