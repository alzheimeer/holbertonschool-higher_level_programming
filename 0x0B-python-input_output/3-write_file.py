#!/usr/bin/python3


def write_file(filename="", text=""):
    '''writes a string to a text file and ret the number of char written'''
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
