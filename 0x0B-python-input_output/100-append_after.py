#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    '''Insert text after each line containing a given string in a file'''
    with open(filename, 'r', encoding='utf-8') as f:
        pepe = f.readlines()
    with open(filename, "w", encoding="utf-8") as f:
        for a in pepe:
            f.write(a)
            if (search_string in a):
                f.write(new_string)
