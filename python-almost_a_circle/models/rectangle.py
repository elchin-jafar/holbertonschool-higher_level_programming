#!/usr/bin/python3

"""rectangle class module"""


from models.base import Base


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.integer_validator("x", x)
        self.integer_validator("y", y)
        self.is_zero_or_lower("width", width)
        self.is_zero_or_lower("height", height)
        self.is_lower_than_zero("x", x)
        self.is_lower_than_zero("y", y)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.is_zero_or_lower("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.is_zero_or_lower("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.is_lower_than_zero("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.is_lower_than_zero("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        """checks value input if it has int type or not"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    def is_zero_or_lower(self, name, value):
        """raises error if value is equal or lower than 0"""

        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def is_lower_than_zero(self, name, value):
        """raises error if value is lower than 0"""

        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """returns the area of rectangle"""

        return self.__width * self.__height
