#!/usr/bin/python3
"""
This script takes two arguments: the repository name and the owner name.
It uses the GitHub API to retrieve information about the specified repository.
"""

import requests
import sys


def main():
    """ def com """
    owner = sys.argv[1]
    repo = sys.argv[2]
    limit = 10
    url = f'https://api.github.com/repos\
/{repo}/{owner}/commits?per_page={limit}'

    response = requests.get(url).json()
    for commit in response:
        name = commit.get("commit").get("author").get("name")
        print(f'{commit.get("sha")}: {name}')


if __name__ == "__main__":
    main()
