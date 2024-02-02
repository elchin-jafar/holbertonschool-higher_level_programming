#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    list1 = list(set_1)
    list2 = list(set_2)
    res = list()

    for item in list1:
        if item not in list2:
            res.append(item)

    for item in list2:
        if item not in list1 and item not in res:
            res.append(item)

    return res
