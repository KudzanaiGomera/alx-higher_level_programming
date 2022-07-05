#!/usr/bin/python3

"""
append_write Module
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file, then returns the
    number of characters appended"""
    with open(filename, 'a') as f:
        chars = f.write(text)
    return chars
