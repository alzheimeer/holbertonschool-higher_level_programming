#!/usr/bin/python3


def number_of_lines(filename=""):
    '''returns the number of lines of a text file'''
    with open(filename, 'r', encoding="utf-8") as f:
        readf = len(f.readlines())
    return readf
