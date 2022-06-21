#!/usr/bin/python3
"""
    4-square.py
    This module defines the square
    return {}
"""


class Square():
    """Square class"""

    def __init__(self, size=0):
        """Initializing class"""
        self.size = size

    def area(self):
        """Returning the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Retrieving the size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the size of the Square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Printing the square using stdout the square with the char #"""
        if self.__size == 0:
            print()
            return
        else:
            for x in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print()
