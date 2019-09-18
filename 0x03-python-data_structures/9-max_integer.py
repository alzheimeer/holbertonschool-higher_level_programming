#!/usr/bin/python3
def max_integer(my_list=[]):
    l = len(my_list)
    if l == 0:
        return(None)
    my_list.sort()
    return(my_list[-1])
