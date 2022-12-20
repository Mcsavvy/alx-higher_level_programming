#!/usr/bin/python3

"""
1. Square with size validation
    Contains a 'Square' class that defines a square which accepts
    a size at instantiation
"""


class Square:
    """
    An square class that accepts a size
    """

    def __init__(self, size=0):
        """
        initialize class with size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
