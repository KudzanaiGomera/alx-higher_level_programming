#!/usr/bin/python3

"""
pascal_triangle Module
"""


def pascal_triangle(n):
    """Returns a list of lists of integers of n"""
    res = []
    if n <= 0:
        return res
    for x in range(n):
        row = [1]
        if x > 0:
            for j in range(x):
                row.append(sum(res[-1][j:j + 2]))
        res.append(row)
    return res
