#!/usr/bin/python3
import sys
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
    else:
        print("{0} arguments:".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{0}: {1}".format(i, sys.argv[i]))
