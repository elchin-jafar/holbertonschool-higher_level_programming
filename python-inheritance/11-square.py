#!/usr/bin/python3

"""square module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class based on rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[{}] {}/{}".format(self.__class__.__name__, self.__size, self.__size)
