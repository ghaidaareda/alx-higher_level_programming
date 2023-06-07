#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for i in str:
        if ord(i) in range(97, 123):
            upper_i = chr(ord(i) - 32)
        else:
            upper_i = i
        upper_str += upper_i
        print("{0}".format(upper_i), end="")
    print()
