#!/usr/bin/python3


"""
This file contains a function that adds two integers
add_integer(a, b):
    adds two integers
"""


def add_integer(a, b=98):
    """
    add two integers a and b
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
