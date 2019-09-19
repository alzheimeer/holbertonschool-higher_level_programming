#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if matrix:
        return [list(map(jf, i)) for i in matrix]


def jf(x):
    x = x ** 2
    return(x)
