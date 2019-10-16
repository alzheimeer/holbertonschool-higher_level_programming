#!/usr/bin/python3


def append_write(filename="", text=""):
    '''appends a string at the end of a file and ret number of char added'''
    with open(filename, 'a', encoding="utf-8") as f:
                return f.write(text)
