#!/usr/bin/python3
"""
    Module defining rectangle
    return {}
"""


class Rectangle():
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
