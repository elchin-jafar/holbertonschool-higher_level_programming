#!/usr/bin/python3

""" Defines file opening and reading"""


def read_file(filename=""):
    """ prints the content of text file"""

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
