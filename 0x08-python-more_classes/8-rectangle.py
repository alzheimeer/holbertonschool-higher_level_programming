#!/usr/bin/python3
"""Creating an empty Class"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"
    """Print a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the object"""
        type(self).number_of_instances += 1
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
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * self.__width + 2 * self.__height

        return perimeter

    def __str__(self):
        """Representation of rectangle"""
        s = ""
        if self.__width == 0 or self.__height == 0:
            s = ""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    s += str(self.print_symbol)
                if i != self.__height - 1:
                    s += '\n'
            return s

    def __repr__(self):
        """eval"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """delete instance"""
        type(self).number_of_instances -= 1
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
