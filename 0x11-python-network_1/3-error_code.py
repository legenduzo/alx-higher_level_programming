#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == '__main__':
    url = argv[1]

    try:
        with urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except HTTPError as e:
        print(f"Error code: {e.code}")
