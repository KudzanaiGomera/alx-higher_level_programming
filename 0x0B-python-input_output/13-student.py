#!/usr/bin/python3

"""
Student class Module
"""


class Student:
    """A student class."""

    def __init__(self, first_name, last_name, age):
        """Initialization of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrievinf the dictionary representation of the Student instance"""
        if attrs is not None:
            d = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    d[k] = v
            return d
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for k, v in json.items():
            self.__dict__[k] = v
