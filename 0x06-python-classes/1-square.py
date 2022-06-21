#!/usr/bin/python3
"""
    1-square.py
    This module defines a square with a private instance size
    return {}
"""


class Square:
    """Square class
       This defines a square with a private instance size
    """
    def __init__(self, size):
        """Initializes the data."""
        self.__size = size
