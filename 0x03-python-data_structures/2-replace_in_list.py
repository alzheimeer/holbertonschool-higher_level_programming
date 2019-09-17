#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    lenx = len(my_list)
    if idx < 0:
        return (my_list)
    elif idx > lenx - 1:
        return (my_list)
    my_list[idx] = element
    return (my_list)
