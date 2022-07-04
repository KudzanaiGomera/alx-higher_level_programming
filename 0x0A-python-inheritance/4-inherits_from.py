#!/usr/bin/python3

"""
inherits_from Module
"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of the class that inherited from"""
    return isinstance(obj, a_class) and type(obj) != a_class
