#!/usr/bin/python3

def add_integer(a, b=98):
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
