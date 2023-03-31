#!/bin/bash
# a script that prints the body of a successful request
status_code="$(curl -sI $1 | head -1 | cut -d ' ' --fields=2)"
if [ $status_code == '200' ]; then
	echo "$(curl -s $1)"
fi
