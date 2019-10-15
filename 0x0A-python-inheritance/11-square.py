#!/usr/bin/python3


class BaseGeometry():
    '''Class'''
    def area(self):
        '''Raise exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value'''
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    '''class Rectangle'''
    def __init__(self, width, height):
        '''ini'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''area'''
        return self.__width * self.__height

    def __str__(self):
        '''print human'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)


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

    def __str__(self):
        '''print str'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
