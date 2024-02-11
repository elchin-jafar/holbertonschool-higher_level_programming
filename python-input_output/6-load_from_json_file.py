#!/usr/bin/python3

"""placeholder"""


import json


def load_from_json_file(filename):
    """placeholder"""

    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
