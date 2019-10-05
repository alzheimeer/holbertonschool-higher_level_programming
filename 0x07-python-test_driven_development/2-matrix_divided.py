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
    mt = "matrix must be a matrix (list of lists) of integers/floats"
    ms = "Each row of the matrix must have the same size"
    lengh = 0
    if not matrix or not isinstance(matrix, list):
        raise TypeError(mt)
    for row in matrix:
        if lengh != 0 and len(row) != lengh:
            raise TypeError(ms)
        if not row or not isinstance(row, list):
            raise TypeError(mt)
        for col in row:
            if not type(col) in (int, float):
                raise TypeError(mt)
    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    lengh = len(row)
    m = []
    for x in matrix:
        m.append(list(map(lambda y: round(y / div, 2), x)))
    return m
