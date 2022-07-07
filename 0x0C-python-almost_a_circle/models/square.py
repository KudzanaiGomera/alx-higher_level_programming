#!/usr/bin/python3

"""
Square Module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of teh class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the class"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """Size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Assign an argument to all attributes"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, attrs[i], e)
            return
        for x, y in kwargs.items():
            if hasattr(self, x):
                setattr(self, x, y)

    def to_dictionary(self):
        """Returns a dictionary representation of the class"""
        d = {}
        for x, y in vars(self).items():
            if x.startswith("_"):
                if not x.endswith("width") and not x.endswith("height"):
                    idx = x.index("__")
                    d[x[idx + 2:]] = y
                else:
                    d["size"] = y
            else:
                d[x] = y
        return d
