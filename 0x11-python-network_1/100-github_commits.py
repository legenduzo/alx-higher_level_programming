#!/usr/bin/python3
"""
list 10 most recent commits
"""
from sys import argv
import requests


if __name__ == "__main__":
    repository = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/"
    endpoint = f"{owner}/{repository}/commits?per_page=10"

    response = requests.get(f'{url}{endpoint}')
    commits = response.json()

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
