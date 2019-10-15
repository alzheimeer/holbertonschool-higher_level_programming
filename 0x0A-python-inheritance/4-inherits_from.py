#!/usr/bin/python3


def inherits_from(obj, a_class):
    '''object is an instance of a class that inherited'''
    return isinstance(obj, a_class) and type(obj) is not a_class
