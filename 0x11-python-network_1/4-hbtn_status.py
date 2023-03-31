#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
and displayes the response
"""

if __name__ == "__main__":
    import requests

    URL = "https://alx-intranet.hbtn.io/status"

    with requests.get(URL) as response:
        content = response.text
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
