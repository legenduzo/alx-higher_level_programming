#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
from requests import get

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = get(url)
    content = response.text

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
