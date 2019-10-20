#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    '''class Rectangle that inherits from Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''getter width'''
        return self.__width

    @width.setter
    def width(self, v):
        '''setter width'''
        self.__width = v

    @property
    def height(self):
        '''getter height'''
        return self.__height

    @height.setter
    def height(self, v):
        '''setter height'''
        self.__height = v

    @property
    def x(self):
        '''getter x'''
        return self.__x

    @x.setter
    def x(self, v):
        '''setter x'''
        self.__width = v

    @property
    def y(self):
        '''getter y'''
        return self.__y

    @width.setter
    def y(self, v):
        '''setter y'''
        self.__y = v
