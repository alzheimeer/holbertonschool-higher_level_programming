#!/usr/bin/python3
def roman_to_int(num):
    listax = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r = 0
    for i,c in enumerate(num):
        if (i+1) == len(num) or listax[c] >= listax[num[i+1]]:
            r += listax[c]
        else:
            r -= listax[c]
    return r
