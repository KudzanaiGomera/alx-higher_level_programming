#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if matrix:
        result = []
        for row in matrix:
            squared = []
            for x in row:
                squared.append(x ** 2)
            result.append(squared)
    return result
