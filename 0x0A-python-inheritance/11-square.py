#!/usr/bin/python3

"""
Square Module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """Initializion of the  class."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of the class"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
