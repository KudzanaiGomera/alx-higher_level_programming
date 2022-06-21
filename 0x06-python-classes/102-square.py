#!/usr/bin/python3
"""
    This module defines linked lists
    return {}
"""


class Square():
    """square class"""

    def __init__(self, size=0):
        """Initialization class"""
        self.size = size

    def area(self):
        """Returning the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Retrieving the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the size of the square"""
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be an number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Overload equal operator."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Overload not equal operator."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Overload greater than operator."""
        return self.area() > other.area()

    def __lt__(self, other):
        """Overload less than operator."""
        return self.area() < other.area()

    def __ge__(self, other):
        """Overload greater than or equal operator."""
        return self.area() >= other.area()

    def __le__(self, other):
        """Overload less than or equal operator."""
        return self.area() <= other.area()
