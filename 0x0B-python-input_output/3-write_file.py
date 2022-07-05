#!/usr/bin/python3

"""
write_file Module
"""


def write_file(filename="", text=""):
    """Writes a string to the text file, and then returns the number of
    characters that we wrote in"""
    with open(filename, 'w') as f:
        chars = f.write(text)
    return chars
