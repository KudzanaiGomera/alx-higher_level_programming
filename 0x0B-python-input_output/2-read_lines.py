#!/usr/bin/python3

"""
read_lines Module
"""


def read_lines(filename="", nb_lines=0):
    """Reads a set number of lines in a text file, then prints it"""
    with open(filename, 'r') as f:
        if nb_lines <= 0 or nb_lines >= len(open(filename).readlines()):
            nb_lines = len(open(filename).readlines())
        for x in range(nb_lines, 0, -1):
            print(f.readline(), end="")
