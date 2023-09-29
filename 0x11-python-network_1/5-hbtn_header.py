#!/usr/bin/python3
"""
This script takes a URL as input, sends a request to the URL,
and displays the value of the X-Request-Id variable in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id is not None:
        print(x_request_id)
