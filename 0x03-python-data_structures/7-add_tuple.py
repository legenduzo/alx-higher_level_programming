#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = 0
    if len(tuple_a) > 0 and isinstance(tuple_a[0], int):
        a1 = tuple_a[0]
    a2 = 0
    if len(tuple_a) > 1 and isinstance(tuple_a[1], int):
        a2 = tuple_a[1]
    b1 = 0
    if len(tuple_b) > 0 and isinstance(tuple_b[0], int):
        b1 = tuple_b[0]
    b2 = 0
    if len(tuple_b) > 1 and isinstance(tuple_b[1], int):
        b2 = tuple_b[1]
    a = a1 + b1
    b = a2 + b2
    return (a, b)
