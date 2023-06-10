#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_list = list(my_string)
        for i in new_list.copy():
            if i == "c" or i == "C":
                new_list.remove(i)
        return("".join(new_list))
