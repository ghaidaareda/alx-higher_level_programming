#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request
import requests
if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        response = requests.get('https://alx-intranet.hbtn.io/status')
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", response.content)
        print("\t- utf8 content:", response.content.decode('utf8'))