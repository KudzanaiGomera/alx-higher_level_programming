#!/usr/bin/python3

"""
This module contains matrix_mul functions
"""


def matrix_mul(m_a, m_b):
    """multiply 2 matrix"""
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if not len(m_a):
        raise ValueError("m_a can't be empty")
    if not len(m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(x, list) for x in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(x, list) for x in m_b):
        raise TypeError('m_b must be a list of lists')
    if any(not len(x) for x in m_a):
        raise ValueError("m_a can't be empty")
    if any(not len(x) for x in m_b):
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError('m_a should contain only integers or floats')
    for row in m_b:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError('m_b should contain only integers or floats')
    len_rows = list(map(lambda x: len(x), [x for x in m_a]))
    if len_rows.count(len_rows[0]) != len(len_rows):
        raise TypeError('each row of m_a must should be of the same size')
    len_rows = list(map(lambda x: len(x), [x for x in m_b]))
    if len_rows.count(len_rows[0]) != len(len_rows):
        raise TypeError('each row of m_b must should be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a * b for a, b in zip(A_row, B_col))
               for B_col in zip(*m_b)]
              for A_row in m_a]
    return result
