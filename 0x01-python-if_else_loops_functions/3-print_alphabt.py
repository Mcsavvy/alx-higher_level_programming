#!/usr/bin/python3
for n in range(ord('a'), ord('z') + 1):
    if n not in (ord('e'), ord('q')):
        print("{}".format(chr(n)), end='')
