#!/usr/bin/python3
"""
This module has a function that divides a matrix
"""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix
    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix
    """
    ms = "Each row of the matrix must have the same size"
    s = 'matrix must be a matrix (list of lists) of integers/floats'
    if not matrix or not isinstance(matrix, list):
        raise TypeError(s)
    for row in matrix:
        if isinstance(row, list) and row:
            for col in row:
                if not isinstance(col, int) and not isinstance(col, float):
                    raise TypeError(s)
        else:
            raise TypeError(s)

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError(ms)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    m = []
    for x in matrix:
        m.append(list(map(lambda y: round(y / div, 2), x)))
    return m
