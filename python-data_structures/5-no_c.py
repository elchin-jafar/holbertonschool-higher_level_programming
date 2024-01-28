#!/usr/bin/python3
def no_c(my_string):
    res = str()
    for char in my_string:
        if ord(char) == 67 or ord(char) == 99:
            continue
        res += char
    return res
