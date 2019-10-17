#!/usr/bin/python3


def pascal_triangle(row):
    '''ret a list of lists of integers representing Pascal’s triangle of n'''
    if row <= 0:
        return []
    elif row == 1:
        return [[1]]
    result = [[1]]
    while len(result) != row:
        last_row = result[-1]
        new_row = [1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row += [1]
        result.append(new_row)

    return result
