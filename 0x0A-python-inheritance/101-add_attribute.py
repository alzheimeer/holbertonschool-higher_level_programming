#!/usr/bin/python3


def add_attribute(obj, key, value):
    '''add atribute'''
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
