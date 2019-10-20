#!/usr/bin/python3

class Base():
    """Base class manage id attribute in all classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
