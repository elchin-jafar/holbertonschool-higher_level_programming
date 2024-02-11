#!/usr/bin/python3

"""placeholder"""


class Student:
    """placeholder"""

    def __init__(self, first_name, last_name, age):
        """placeholder"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """placeholder"""

        if type(attrs) is list and all([type(x) is str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return (self.__dict__)

    def reload_from_json(self, json):
        for i, j in json.items():
            self.__dict__[i] = j
