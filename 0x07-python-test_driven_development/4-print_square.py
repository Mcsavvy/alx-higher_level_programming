#!/usr/bin/python3


"""
this file contains a function that prints a square
print_square:
    prints a square using the '#' character
"""


def print_square(size):
    """
    this function prints a square using the '#' character
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for r in range(size):
        for c in range(size):
            print('#', end='')
        print()
