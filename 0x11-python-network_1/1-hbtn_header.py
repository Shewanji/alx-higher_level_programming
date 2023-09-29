#!/usr/bin/python3
"""
This script takes a URL as an argument, sends a request to the URL,
and displays the value of the X-Request-Id variable found in the header
of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./1-hbtn_header.py <URL>")

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get('X-Request-Id')

    if x_request_id is not None:
        print(x_request_id)
