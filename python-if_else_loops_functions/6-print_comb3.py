#!/usr/bin/python3
for dig1 in range(10):
    for dig2 in range(dig1, 10):
        if dig1 == dig2:
            continue
        elif dig1 == 8:
            print("{}{}".format(dig1, dig2))
        else:
            print("{}{}".format(dig1, dig2), end=", ")
