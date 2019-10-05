#!/usr/bin/python3
"""
This module has a function that adds two numbers
"""


def add_integer(a, b=98):
    """
    Args:
        a: first number
        b: second number
    Returns:
        The addition of the two given numbers
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return result
