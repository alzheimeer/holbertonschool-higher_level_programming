#!/usr/bin/python3
"""Documentation for a square printing function"""


def print_square(size):
    """print a square
    Args:
        size (int): the side length of the square
    Raises:
        TypeError: when the size passed in is not an integer
        ValueError: when the size is less than 0 (ie negative)
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if not isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print('')
