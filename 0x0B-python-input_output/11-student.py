#!/usr/bin/python3

"""
Student class Module
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
