#!/usr/bin/python3
"""
    2-square.py
    This module defines a square by a private attribute size.
    It raises exception if the size < 0 or the size is a non     integer
    return {}
"""


class Square:
    """Square class
       Defines a square by private instance size
    """
    def __init__(self, size=0):
        """Initializes the data."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
