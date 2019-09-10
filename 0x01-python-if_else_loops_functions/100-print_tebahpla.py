#!/usr/bin/python3
m = 0
for i in range(122, 96, -1):
    print("{}".format(chr(i - m)), end='')
    if m == 32:
        m = 0
    elif m == 0:
        m = 32
