#!/usr/bin/python3
for i in range(0, 100):
    if i in range(0, 10):
        print("{:02d}".format(i), end=", ")
    elif i in range(10, 99):
        print("{}".format(i), end=", ")
    else:
        print(i)
