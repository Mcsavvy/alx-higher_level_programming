#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
and displayes the response
"""

if __name__ == "__main__":
    import urllib.request

    URL = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(URL) as response:
        content = response.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content!r}")
        print(f"\t- utf8 content: {content.decode('utf8')}")
