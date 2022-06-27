#!/usr/bin/python3
"""
     Module defining rectangle
    return {}
"""


class Rectangle():
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize"""
        self.width = width
        self.height = height

    def area(self):
        """Return Rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the current Rectangle area."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

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
