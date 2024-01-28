#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0:
        return None
    elif idx >= length:
        return None
    else:
        return my_list[idx]
