#!/usr/bin/python3
"""
script that adds all arguments to a Python list
and then save them to a file
"""
import sys
import json

from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file
args = sys.argv[1:]
try:
    my_list = load_from_json_file("add_item.json")
except:
    my_list =[]
my_list.extend(args)
save_to_json_file(my_list, "add_item.json")
