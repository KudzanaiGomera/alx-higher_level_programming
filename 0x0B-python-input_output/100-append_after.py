#!/usr/bin/python3

"""
append_after Module
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after it contains a certain string"""
    with open(filename, 'r') as f:
        data = f.readlines()

    output = ""
    for line in data:
        output += line
        if search_string in line:
            output += new_string

    with open(filename, 'w') as f:
        f.write(output)
