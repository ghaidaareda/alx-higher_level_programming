#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    try:
        print(response.text)
    except response.status_code >= 400 as e:
        print("Error code:", response.status_code)
