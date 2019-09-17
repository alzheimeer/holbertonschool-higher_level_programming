#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = my_list.copy()
    lenx = len(my_list)
    if idx < 0:
        return (my_list)
    elif idx > lenx - 1:
        return (my_list)
    newlist[idx] = element
    return (newlist)
