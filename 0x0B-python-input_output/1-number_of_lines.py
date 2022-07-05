#!/usr/bin/python3

"""
number_of_lines Module
"""


def number_of_lines(filename=""):
    """Returns  number of lines in a text file"""
    with open(filename, 'r') as f:
        return(len(list(f)))
