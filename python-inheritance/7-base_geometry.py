#!/usr/bin/python3

"""empty class"""


class BaseGeometry:
    """simple class has 2 instance methods: area, integer_validator"""

    def area(self):
        """just raises Exception error"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates given value by its type and value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
