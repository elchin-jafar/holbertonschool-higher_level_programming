#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res = list()
    for i in range(list_length):
        try:
            cur = my_list_1[i] / my_list_2[i]
        except TypeError:
            cur = 0
            print("wrong type")
        except ZeroDivisionError:
            cur = 0
            print("division by 0")
        except IndexError:
            cur = 0
            print("out of range")
        finally:
            res.append(cur)
    print(res)
