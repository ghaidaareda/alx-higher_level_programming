#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    with requests.get('https://alx-intranet.hbtn.io/status') as response:
        print("Body response:")
        print("\t- type:", type(response.content))
        print("\t- content:", response.content)
        print("\t- utf8 content:", response.content.decode('utf8'))
