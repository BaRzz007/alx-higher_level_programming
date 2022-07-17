#!/usr/bin/python3
"""Contains definition of Square class"""


class Square:
    """Square object blueprint"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square.

        Args:
            size: size of the square object
            position: tuple of 2 integers
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for each in position:
            if type(each) is not int or each < 0:
                raise TypeError("position must be a tuple of\
 2 positive integers")
        self.__position = position

    def area(self):
        """Returns the area of the square

        return:
            area of the square
        """
        return self.__size**2

    @property
    def size(self):
        """Getter method for size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Seeter method for size

        Args:
            value(int): Value to update size of Square object
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints a square to stdout"""

        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                for j in range(self.__size + self.__position[0]):
                    if j < self.__position[0]:
                        print(' ', end="")
                    else:
                        print('#', end="")
                print()

    @property
    def position(self):
        """Getter method for position

        Return: tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter"""
        if type(value) is tuple and len(value) == 2:
            if type(value[0]) is int and type(value[1]) is int:
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
