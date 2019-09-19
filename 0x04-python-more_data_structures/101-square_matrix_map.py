#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(jf, x)), matrix))


def jf(x):
    x = x ** 2
    return(x)
