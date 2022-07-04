#!/usr/bin/python3

"""
BaseGeometry Module
"""


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception if it is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Value Validation"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
