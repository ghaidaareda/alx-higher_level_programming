#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    i = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except Exception as x:
            if isinstance(x, TypeError):
                print("wrong type")
            elif isinstance(x, IndexError):
                print("out of range")
            elif isinstance(x, ZeroDivisionError):
                print("division by 0")
            result = 0
        finally:
            result_list.append(result)
    return result_list
