#!/usr/bin/python3
"""
This script takes your GitHub username and personal access token
as arguments, uses Basic Authentication with the token to access
your GitHub information, and displays your user ID.
"""

import requests
import sys

if __name__ == "__main__":
    args = sys.argv
    url = f"https://api.github.com/user"

    # create a session
    session = requests.Session()

    # set username and password
    session.auth = (args[1], args[2])

    # send request to get user data
    response = session.get(url, headers={})

    data = response.json()

    # print id
    print(data.get("id"))
