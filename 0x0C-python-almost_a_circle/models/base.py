#!/usr/bin/python3
import json
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''JSON string representation of list_dictionaries'''
        if list_dictionaries is None or not list_dictionaries:
           return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        ''' returns the list of the JSON string representation json_string
           *.json_string is a string representing a list of dictionaries
           *.If json_string is None or empty, return an empty list
           *. Otherwise, return the list represented by json_string
        '''
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes the JSON string representation of list_objs to a file
            *.list_objs is a list of instances who inherits of Base
            example: list of Rectangle or list of Square instances
            *.The filename must be: <Class name>.json - example: Rectangle.json
            *.You must use the static method to_json_string (created before)'''
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        ''' returns an instance with all attributes already set
           a.**dictionary can be thought of as a double pointer to a dictionary
           b.To use the update method to assign all attribute create dummy
        '''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy = cls(1, 1)
        elif cls is Square:
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''pepe '''
        from os import path
        filename = cls.__name__ + ".json"
        if not path.isfile(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]


    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file.'''
        filename = cls.__name__ + ".csv"
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        filename = cls.__name__ + ".csv"
        from models.rectangle import Rectangle
        from models.square import Square
        new = []
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                new.append(cls.create(**d))
        return new

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
