#!/bin/bash
# a script that sends a DELETE request to a URL
echo "$(curl -X DELETE -s $1)"
