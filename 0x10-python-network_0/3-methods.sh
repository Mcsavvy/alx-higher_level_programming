#!/bin/bash
# a script that prints out the http methods a url accepts
curl -sIX OPTIONS "$1" | grep -i 'allow' | cut -d ' ' -f2-
