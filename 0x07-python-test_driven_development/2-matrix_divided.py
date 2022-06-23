#!/usr/bin/python3
"""
    2-matrix_divided.py
    This module contains the matrix_dividend function
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of the matrix, and returns a new matrix divided by div
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)" +
                    " of integers/floats")
    len_rows = list(map(lambda x: len(x), [x for x in matrix]))
    if len_rows.count(len_rows[0]) != len(len_rows):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, int) and not isinstance(div, float) or div != div:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_list = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        new_list.append(new_row)
    return new_list
