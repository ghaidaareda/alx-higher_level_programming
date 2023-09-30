#!/usr/bin/python3
"""
script that takes GitHub
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    try:
        json_response = response.json()
        print(f"{json_response.get('id')}")
    except ValueError:
        print("None")
