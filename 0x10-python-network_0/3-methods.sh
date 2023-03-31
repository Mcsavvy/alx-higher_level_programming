#!/bin/bash
# a script that prints out the http methods a url accepts
echo "$(curl -sIX OPTIONS $1 | grep 'allow' | cut -d ' ' --fields=2-)"
