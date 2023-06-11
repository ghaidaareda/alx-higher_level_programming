#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    elif len(tuple_b) == 1 and len(tuple_a) >= 2:
        tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
    elif len(tuple_a) == 1 and len(tuple_b) >= 2:
        tuple_c = (tuple_a[0] + tuple_b[0], 0 + tuple_b[1])
    elif len(tuple_b) == 0 and len(tuple_a) >= 2:
        tuple_c = (tuple_a[0], tuple_a[1])
    elif len(tuple_a) == 0 and len(tuple_b) >= 2:
        tuple_c = (tuple_b[0], tuple_b[1])
    elif len(tuple_a) == 0 and len(tuple_b) == 0:
        tuple_c = (0, 0)
    elif len(tuple_b) == 1 and len(tuple_a) == 0:
        tuple_c = (tuple_b[0] + 0, 0)
    elif len(tuple_a) == 1 and len(tuple_b) == 0:
        tuple_c = (tuple_a[0] + 0, 0)
    return(tuple_c)
