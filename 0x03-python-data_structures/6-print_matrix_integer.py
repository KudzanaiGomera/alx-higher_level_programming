#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for i in x:
            print("{:d}".format(i), end=" " if x[-1] != i else "")
        print()
