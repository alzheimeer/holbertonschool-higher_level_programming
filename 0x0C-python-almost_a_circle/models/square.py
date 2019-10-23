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
        a = ['id', 'size', 'x', 'y']
        count = 0
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
                count += 1
        else:
            for c in args:
                setattr(self, a[count], c)
                count += 1

    def to_dictionary(self):
        """dictionary of a Square"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
