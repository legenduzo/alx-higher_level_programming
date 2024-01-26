#!/usr/bin/python3
"""
takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = argv[2]
    values = {'email': email}
    data = urlencode(values).encode('utf-8')

    req = Request(url, data, method='POST')

    with urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
