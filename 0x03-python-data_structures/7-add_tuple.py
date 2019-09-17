#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    la = len(a)
    lb = len(b)
    if la < 2:
        for i in range(la, 2):
            a.append(0)
    if lb < 2:
        for i in range(lb, 2):
            b.append(0)
    nt = [a[0] + b[0], a[1] + b[1]]
    return (tuple(nt))
