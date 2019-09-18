#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nl = my_list.copy()
    for i in range(len(nl)):
        if nl[i] % 2 != 0:
            nl[i] = False
        else:
            nl[i] = True
    return(nl)
