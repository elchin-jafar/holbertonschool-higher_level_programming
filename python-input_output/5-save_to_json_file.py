#!/usr/bin/python3

"""placeholder"""


import json


def save_to_json_file(my_obj, filename):
    """placeholder"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
