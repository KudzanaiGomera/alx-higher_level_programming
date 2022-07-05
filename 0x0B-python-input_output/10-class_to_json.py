#!/usr/bin/python3

"""
class_to_json Module
"""


def class_to_json(obj):
    """returns a dictionary description with data structures like
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object"""
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    if hasattr(obj, "__slots__"):
        return obj.__slots__
