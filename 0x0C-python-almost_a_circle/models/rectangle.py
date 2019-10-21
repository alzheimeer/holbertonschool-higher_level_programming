#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    '''class Rectangle that inherits from Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) is not int:
            raise TypeError("width must be and integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be and integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be and integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be and integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area rectangle"""
        return self.__width * self.__height

    def display(self):
        '''prints in stdout'''
        for i in range(self.__height):
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        p = '[Rectangle]'+' ('+str(self.id)+') '+str(self.__x)\
+'/'+str(self.__y)+' - '+str(self.__width)+'/'+str(self.__height)
        return(p)
