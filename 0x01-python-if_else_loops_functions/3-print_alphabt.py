#!/usr/bin/python3
for n in range(ord('a'), ord('z') + 1):
    if n in (ord('e'), ord('q')):
        continue
    print(chr(n), end='')
