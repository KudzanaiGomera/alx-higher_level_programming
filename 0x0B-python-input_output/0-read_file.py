#!/usr/bin/python3

"""
read_file Module
"""


def read_file(filename=""):
    "reads a text file (UTF8) and prints it to stdout."
    with open(filename, 'r') as f:
        for x in f:
            print(x, end='')
