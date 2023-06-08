#!/usr/bin/python3
from calculator_1 import add, sub, mul,div

a = 10
b = 5
if  __name__ == '__main__':
    add_result = add(a, b)
    sub_result = sub(a, b)
    mul_result = mul(a, b)
    div_result = div(a, b)
    print("{a} + {b} = {add_result}".format(a=a, b=b, add_result=add_result))
    print("{a} - {b} = {sub_result}".format(a=a, b=b, sub_result=sub_result))
    print("{a} * {b} = {mul_result}".format(a=a, b=b, mul_result=mul_result))
    print("{a} / {b} = {div_result}".format(a=a, b=b, div_result=div_result))
