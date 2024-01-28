#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = list()
    for el in my_list:
        new_list.append(el % 2 == 0)
    return new_list
