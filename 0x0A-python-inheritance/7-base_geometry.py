#!/usr/bin/python3


class BaseGeometry():
    """Class"""
    def area(self):
        """ Raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value'''
        if type(value) is not int:
            raise TypeError(name+ " must be an integer")
        if value <= 0:
            raise ValueError(name+ " must be greater than 0")
