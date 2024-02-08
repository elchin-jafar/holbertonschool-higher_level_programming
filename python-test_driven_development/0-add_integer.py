#!/usr/bin/python3
"""add 2 integers"""


def add_integer(a, b=98):
    """
    adds a and b and return sum of them
    checks for type errors
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
