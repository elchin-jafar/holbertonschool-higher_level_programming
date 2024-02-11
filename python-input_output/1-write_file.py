#!/usr/bin/python3

"""placeholder"""


def write_file(filename="", text=""):
    """write text to filename"""

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
