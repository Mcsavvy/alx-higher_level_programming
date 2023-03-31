#!/bin/bash
# A bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sX POST --json "@$2" "$1"
