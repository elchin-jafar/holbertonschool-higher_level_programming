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
        self.integer_validator("width", value)
        self.is_zero_or_lower("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            updates objects' fields according
            to passed arguments to update (this) method
        """

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        if args and len(args) > 0:
            return

        for k, v in kwargs.items():
            if k == "id":
                self.id = v
            elif k == "size":
                self.width = v
            elif k == "x":
                self.x = v
            elif k == "y":
                self.y = v
