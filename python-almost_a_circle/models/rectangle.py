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

    def display(self):
        """displays rectangle with #"""
        for y in range(self.y):
            print("")
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """defines what to print when try print instance of this class"""

        name = self.__class__.__name__
        id = self.id
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        return "[{}] ({}) {}/{} - {}/{}".format(name, id, x, y, width, height)

    def update(self, *args, **kwargs):
        """update instances"""

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

        if args and len(args) > 0:
            return

        for k, v in kwargs.items():
            if k == "id":
                self.id = v
            elif k == "width":
                self.width = v
            elif k == "height":
                self.height = v
            elif k == "x":
                self.x = v
            elif k == "y":
                self.y = v
