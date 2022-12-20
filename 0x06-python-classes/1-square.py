#!/usr/bin/python3

"""
1. Square with size
    Contains a 'Square' class that defines a square which accepts
    a size at instantiation
"""


class Square:
    """
    An square class that accepts a size
    """

    def __init__(self, size):
        """
        initialize class with size
        """
        self.__size = size
