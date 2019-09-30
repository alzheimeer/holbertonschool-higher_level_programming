#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    s = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            s += 1
        except TypeError:
            continue
        except ValueError:
            continue
    print()
    return s
