#!/usr/bin/python3

def exchange(roman):
    switcher = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            }
    return switcher.get(roman)


def roman_to_int(roman_string):
    res = 0

    if (not isinstance(roman_string, str) or roman_string is None):
        return 0

    for i in range(len(roman_string)):
        if (i != len(roman_string) - 1 and
                exchange(roman_string[i]) < exchange(roman_string[i + 1])):
            res += exchange(roman_string[i]) * -1
        elif (i != len(roman_string) - 1 and
                exchange(roman_string[i]) >= exchange(roman_string[i + 1])):
            res += exchange(roman_string[i])
        else:
            res += exchange(roman_string[i])
    return res
