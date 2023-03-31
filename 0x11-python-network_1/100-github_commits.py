#!/usr/bin/python3
"""
This script lists the 10 most recent commit from a repo
"""

if __name__ == "__main__":
    import sys
    import requests

    # read in username and token
    repo, owner = sys.argv[1:]

    # create headers
    # https://docs.github.com/en/rest/users/users?apiVersion=2022-11-28
    headers = {
        "Accept": "application/vnd.github+json",
        "X-Github-Api-Version": "2022-11-28"
    }
    # construct url
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=10"
    with requests.get(url, headers=headers) as response:
        body = response.json()
        for commit in body:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
