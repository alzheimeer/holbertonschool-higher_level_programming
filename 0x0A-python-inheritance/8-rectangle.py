#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class BaseGeometry():
    """ Class that defines a rectangle from BaseGeometry Class """


class Rectangle(BaseGeometry):
    '''class Rectangle'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
