#!/usr/bin/python3
def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    else:
        v = len(list_of_integers)
        mid = v//2
        list_of_integers.sort()
        max_value = list_of_integers[mid]
        for item in list_of_integers[mid:v]:
            if item > max_value:
                max_value = item
        return (max_value)
