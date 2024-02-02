#!/usr/bin/python3

def common_elements(set_1, set_2):
    list1 = list(set_1)
    list2 = list(set_2)
    res = list()

    for i in range(len(list1)):
        if (len(list1) != 0 and len(list2) != 0 and list1[i] == list2[i]):
            res.append(list1[i])
    return res
