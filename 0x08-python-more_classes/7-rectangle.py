#!/usr/bin/python3
"""
    Module defining rectangle
    return {}
"""


class Rectangle():
    """A rectangle class"""

    # A class variable, counting the number of rectangles
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize class"""
        self.width = width
        self.height = height

        # when a rectangle is created, the rectangle
        # adds to its number of instances
        Rectangle.number_of_instances += 1

    def area(self):
        """Return Rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return Rectangle area"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    @property
    def width(self):
        """Retrieve width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """Print the rectangle with the char #"""
        if self.__height == 0 or self.__width == 0:
            return("")
        else:
            str1 = ""
            for x in range(self.__height):
                for y in range(self.__width):
                    str1 += str(self.print_symbol)
                str1 += "\n"
        return(str1[:-1])

    def __repr__(self):
        """Get string evaluation of the rectangle"""
        if self.__height == 0 or self.__height == 0:
            return("")
        else:
            return("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Prints when the instance of the Rectangle is deleted"""
        # when the rectangle is deleted, number of instances are decreased
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
