#!/bin/bash
# printing the size of an http response
curl -sI "$1" | grep -i 'content-length' | cut -d ' ' -f2
