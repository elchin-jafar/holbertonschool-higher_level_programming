#!/usr/bin/python3

"""placeholder"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert list of dictionary to json string (serialize)"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """placeholder"""

        filename = "{}.json".format(cls.__name__)

        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write('[]')
            else:
                list = [instance.to_dictionary() for instance in list_objs]
                serialized_result = Base.to_json_string(list)
                jsonfile.write(serialized_result)
