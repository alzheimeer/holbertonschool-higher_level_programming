#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    '''reads n lines of a text file (UTF8) and prints it to stdout'''
    with open(filename, 'r', encoding="utf-8") as f:
        if nb_lines <= 0:
            pepe = f.readlines()
            for i in pepe:
                print(i, end='')
        else:
            pepe = f.readlines()[0:nb_lines]
            for i in pepe:
                print(i, end='')
