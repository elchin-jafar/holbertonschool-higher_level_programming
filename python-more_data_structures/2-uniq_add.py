#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    res = 0
    for num in uniq_list:
        res += num
    return res
