#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the
response.
"""

if __name__ == "__main__":
    import requests
    import sys

    URL = sys.argv[1]

    with requests.get(URL) as response:
        print(response.headers.get("X-Request-Id"))
