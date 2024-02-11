#!/usr/bin/python3

"""this module is about creating list with inheritin list class"""


class MyList(list):
    """class which inherits superclass list"""

    def print_sorted(self):
        """prints ordered list"""

        if issubclass(MyList, list):
            print(sorted(self))
