#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

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
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 4:
                self.x = args[2]
            if len(args) == 5:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary of a Square"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
