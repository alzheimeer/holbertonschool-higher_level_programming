#!/usr/bin/python3
"""
Class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Print Rectangle"""
        return "[Square] (" + str(self.id) + ") " + str(self.x) \
            + "/" + str(self.y) + " - " + str(self.size)

    @property
    def size(self):
        """getters size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updating variable arguments"""
        j = ['id', 'size', 'x', 'y']
        i = 0
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
                i += 1
        if args:
            for c in args:
                setattr(self, j[i], c)
                i += 1

    def to_dictionary(self):
        """dictionary of a Square"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
