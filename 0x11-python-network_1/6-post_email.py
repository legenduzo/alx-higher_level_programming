#!/usr/bin/python3
"""
takes in a URL and an email address, sends a POST request
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
