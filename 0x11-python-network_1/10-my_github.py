#!/usr/bin/python3
"""
takes your GitHub credentials and displays your id
"""
import requests
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    token = argv[2]
    headers = {'Authorization': f'Bearer {token}'}
    res = requests.get("https://api.github.com/user", headers=headers)
    if (res.status_code >= 400):
        print("None")
        exit()
    print(res.json()["id"])
