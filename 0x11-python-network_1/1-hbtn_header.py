#!/usr/bin/python3
''' displays the value of the X-Request-Id variable '''
from urllib.request import urlopen
from sys import argv


if __name__ == '__main__':
    """ Print response """
    url = argv[1]

    with urlopen(url) as response:
        request_id = response.getheader('X-Request-Id')
        print(request_id)
