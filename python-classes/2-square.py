#!/usr/bin/python3
"""check if field has normal value and typ"""


class Square:
    """body of class"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
