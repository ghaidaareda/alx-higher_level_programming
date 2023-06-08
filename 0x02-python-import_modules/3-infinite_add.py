#!/usr/bin/python3
import sys
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("0")
    else:
        result = 0
        for i in range(1, len(sys.argv)):
            args = int(sys.argv[i])
            result += args
        print("{0}".format(result))
