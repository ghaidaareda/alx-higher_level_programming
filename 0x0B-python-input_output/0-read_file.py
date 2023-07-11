#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        file_content = f.read().rstrip('\n')
        print(file_content)
    f.close()
