#!/usr/bin/python3
"""
    This module defines linked lists
    return {}
"""


class Square():
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Class Initialization"""
        self.size = size
        self.position = position

    def area(self):
        """Returning the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Retrieving the size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the size of Square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Printing the square with the char #"""
        if self.__size == 0:
            print()
            return
        for row in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        """Retrieving the position of Square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setting the position of Square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(isinstance(value, int) and num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __repr__(self):
        string = ""
        if self.__size == 0:
            return ""
        for row in range(self.__position[1]):
            string += "\n"
        for x in range(self.__size):
            for space in range(self.__position[0]):
                string += " "
            for i in range(self.__size):
                string += "#"
            string += "\n"
        return string[:-1]
