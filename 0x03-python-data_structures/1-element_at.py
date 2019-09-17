#!/usr/bin/python3
def element_at(my_list, idx):
    lenx = len(my_list)
    if idx < 0:
        return(None)
    elif idx > lenx:
        return(None)
    i = my_list[idx]
    return(i)
