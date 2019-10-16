#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class square'''
    def __init__(self, size):
        '''ini'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''area'''
        return self.__size * self.__size
