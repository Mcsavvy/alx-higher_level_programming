#/bin/bash
# printing the size of an http response
echo $(curl -sI $1 | grep 'content-length' | cut -d ' ' --fields=2)

