#!/usr/bin/python3
"""
This file provides a class which is a circle interface
"""


import math


class MagicClass:
    """
    An interface representing a circle
    """
    def __init__(self, radius=0):
        """
        initialize a circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        return the area of a circle
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        return the circumference of a circle
        """
        return 2 * math.pi * self.__radius
