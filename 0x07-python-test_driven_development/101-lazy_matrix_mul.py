#!/usr/bin/python3
"""
module that has matrix operations
"""


def lazy_matrix_mul(m_a, m_b):
    """ Dot product with numpy"""
    import numpy
    return numpy.matmul(m_a, m_b)
