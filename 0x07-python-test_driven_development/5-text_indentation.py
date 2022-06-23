#!/usr/bin/python3

"""
This module contains text_indentation function
"""


def text_indentation(text):
    """
    Prints text after the characters ., ? , : in addition to 2 new lines
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    beg = 0
    for i, c in enumerate(text):
        if i == len(text) - 1:
            print(text[beg:i + 1].strip(), end="")
        elif c in ".?:":
            print(text[beg:i + 1].strip(), end="\n\n")
            beg = i + 1
