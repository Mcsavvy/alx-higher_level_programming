#!/bin/bash
# a script that prints the body of a successful request
if [ "$(curl -sI $1 | head -1 | cut -d ' ' --fields=2)" == '200' ]; then echo "$(curl -s $1)"; fi
