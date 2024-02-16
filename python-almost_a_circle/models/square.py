#!/usr/bin/python3

"""defines square - spacial form of rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """defines square class inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize square"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """defines output of printing instances of this class"""

        name = self.__class__.__name__
        id = self.id
        x = self.x
        y = self.y
        size = self.size
        return "[{}] ({}) {}/{} - {}".format(name, id, x, y, size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.integer_validator("size", value)
        self.is_zero_or_lower("size", value)
        self.width = value
        self.height = value
