#!/usr/bin/python3
import json


class Base():
    """Base class manage id attribute in all classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        '''JSON string representation of list_dictionaries'''
        if list_dictionaries is None or not list_dictionaries:
           return "[]"
        return json.dumps(list_dictionaries)

    
