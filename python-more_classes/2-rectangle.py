#!/usr/bin/python3

"""Define width and height of rectangle"""


class Rectangle:
    """Simple Rectangle with width and height attributes"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for private width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
