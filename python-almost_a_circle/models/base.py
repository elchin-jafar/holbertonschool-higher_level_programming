#!/usr/bin/python3

"""placeholder"""


class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
