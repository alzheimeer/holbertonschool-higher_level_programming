#!/usr/bin/python3
"""
Matrix_mul
"""


def matrix_mul(m_a, m_b):
    """Dot multiply 2 matrices"""
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    for rows in m_a:
        if not isinstance(rows, list):
            raise TypeError('m_a must be a list of lists')
        for col in rows:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError('m_a should contain only integers or floats')
    for rows in m_b:
        if not isinstance(rows, list):
            raise TypeError('m_b must be a list of lists')
        for col in rows:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError('m_b should contain only integers or floats')
    if m_a == [] or m_a == [[]]:
        raise ValueError('m_a can\'t be empty')
    elif m_b == [] or m_b == [[]]:
        raise ValueError('m_b can\'t be empty')

    rowsA = len(m_a)
    colsA = len(m_a[0])
    rowsB = len(m_b)
    colsB = len(m_b[0])

    for rows in m_a:
        if len(rows) != colsA:
            raise TypeError('each row of m_a must be of the same size')
    for rows in m_b:
        if len(rows) != colsB:
            raise TypeError('each row of m_b must be of the same size')

    if colsA != rowsB:
        raise ValueError('m_a and m_b can\'t be multiplied')

    m_c = [[0 for i in range(colsB)] for j in range(rowsA)]

    for i in range(rowsA):
        for j in range(colsB):
            for k in range(rowsB):
                m_c[i][j] += m_a[i][k] * m_b[k][j]

    return m_c
