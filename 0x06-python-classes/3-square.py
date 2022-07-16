#!/usr/bin/python3
"""Contains definition of Square class"""


class Square:
    """Square object blueprint"""

    def __init__(self, size=0):
        """Initializes the square.

        Args:
            size: size of the square object
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the are of the square

        return:
            area of the square
        """
        return self.__size**2
