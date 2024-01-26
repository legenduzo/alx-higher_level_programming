#!/usr/bin/python3
"""
takes in a letter and sends a POST request
"""
from requests import post
from sys import argv

if __name__ == "__main__":
    q = argv[1] if len(argv) > 1 else ""
    response = post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        resp = response.json()
        if resp:
            print(f"[{resp.get('id')}] {resp.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
