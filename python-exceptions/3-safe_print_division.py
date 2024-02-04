#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        try:
            print("Inside result: {:.1f}".format(res))
        except TypeError:
            print("Inside result: None")

    return res
