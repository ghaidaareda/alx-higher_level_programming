#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_a = ()
    if sentence:
        tuple_a = (len(sentence), sentence[0])
    else:
        tuple_a = (0, None)
    return tuple_a
