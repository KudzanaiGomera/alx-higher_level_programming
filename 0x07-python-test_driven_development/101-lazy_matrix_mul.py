#!/usr/bin/python3

"""
This module contains lazy_matrix_mul function
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply 2 matrix using the NumPy
    """
    return np.matmul(m_a, m_b)
