#!/usr/bin/python3
"""
    0-add_integer.py
    This module contains add_integer functions
"""


def add_integer(a, b=98):
    """
    Return the sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
