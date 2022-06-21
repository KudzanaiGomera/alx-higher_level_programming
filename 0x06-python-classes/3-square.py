#!/usr/bin/python3
"""
    3-square.py
    This module defines a square
    return size
"""


class Square:
    """Square class
      Defining a square
       return size
    """
    def __init__(self, size=0):
        """Initializes the data
           return size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
