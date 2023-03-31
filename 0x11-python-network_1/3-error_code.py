#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    URL = sys.argv[1]

    try:
        with urllib.request.urlopen(URL) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")
