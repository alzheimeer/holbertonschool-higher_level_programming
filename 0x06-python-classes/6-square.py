#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return (self.__size**2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.size == 0:
            print()
        for l in range(self.__position[1]):
            print()
        else:
            for i in range(self.size):
                for j in range(self.size+self.__position[0]):
                    if j < self.position[0]:
                        print(" ", end='')
                    else:
                        print("#", end='')
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, int) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
