#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_value = max(a_dictionary.values())
    res = [key for key, value in a_dictionary.items() if value == max_value]
    if res:
        return res[0]
    else:
        return None
