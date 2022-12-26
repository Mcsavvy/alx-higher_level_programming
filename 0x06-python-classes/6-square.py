#!/usr/bin/python3

"""
Square with size validation and position validation
"""


class Square:
    """
    An square class that accepts a size
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initialize class with size
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        get size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        retrieve to position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        set square position
        """
        if not isinstance(value, tuple) or \
                len(value) != 2 or not \
                all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        calculate the area of a square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square
        with the character '#'
        """
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            for _ in range(self.position[0]):
                print(" ", end="")
            for _ in range(self.size):
                print("#", end="")
            print()
