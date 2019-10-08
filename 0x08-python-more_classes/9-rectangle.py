#!/usr/bin/python3
"""Creating an empty Class"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"
    """Print a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the object"""
        Rectangle.number_of_instances += 1
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
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Make private"""
        return self.__height

    @height.setter
    def height(self, value):
        """Handle errors"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculate area of rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Get string representation of rectangle."""
        s = ""
        if self.__width == 0 or self.__height == 0:
            return s
        for row in range(self.__height):
            for char in range(self.__width):
                s += '#'
            s += '\n'
        return s[:-1]

    def __repr__(self):
        """eval"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """delete instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ rectangle with width = height"""
        return cls(size, size)
