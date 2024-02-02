#!/usr/bin/python3

def common_elements(set_1, set_2):
    list1 = list(set_1)
    list2 = list(set_2)
    res = list()

    for item in list1:
        if item in list2:
            res.append(item)

    return res
