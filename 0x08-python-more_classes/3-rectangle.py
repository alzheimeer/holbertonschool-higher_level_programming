#!/usr/bin/python3
"""Creating an empty Class"""


class Rectangle:
    """Print a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the object"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Make private"""
        return self.__width

    @width.setter
    def width(self, value):
        """Handle errors"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Make private"""
        return self.__height

    @height.setter
    def height(self, value):
        """Handle errors"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Representation of rectangle"""
        s = ""
        if self.__width == 0 or self.__height == 0:
            s = ""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    s += '#'
                if i != self.__height - 1:
                    s += '\n'
            return s
