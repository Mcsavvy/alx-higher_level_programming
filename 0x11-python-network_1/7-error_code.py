#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    import requests
    import sys

    URL = sys.argv[1]

    with requests.get(URL) as response:
        if response.ok:
            print(response.text)
        else:
            print(f"Error code: {response.status_code}")
