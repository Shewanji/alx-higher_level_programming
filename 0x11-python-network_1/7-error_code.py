#!/usr/bin/python3
"""
This script takes a URL as input, sends a request to the URL,
and displays the body of the response. If the HTTP status code
is greater than or equal to 400, it prints an error message.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    content = response.text

    print(content)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
