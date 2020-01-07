#!/usr/bin/python3
def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    else:
        v = len(list_of_integers)
        list_of_integers.sort()
        max_value = list_of_integers[v-1]
        return (max_value)
