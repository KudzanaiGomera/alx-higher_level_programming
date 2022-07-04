#!/usr/bin/python3

"""
MyList module
"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        print(sorted(self))
