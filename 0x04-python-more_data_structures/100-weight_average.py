#!/usr/bin/python3
def weight_average(my_list=[]):
    z , y = 0, 0
    if my_list == []:
        return 0
    for x, m in my_list:
        z += (x * m)
        y += (m)
    z /= y
    return (z)
