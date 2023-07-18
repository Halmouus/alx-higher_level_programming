#!/usr/bin/python3
"""Square module. A class inheriting from
Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class for the Square object"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        "string representation of a Square object"
        return (f"[Square] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}")

    @property
    def size(self):
        """property to retrieve the size"""
        return self.width

    @size.setter
    def size(self, value):
        """property to set the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        "updates a Square object"
        attrs = ["id", "size", "x", "y"]
        if args and len(args) > 0 and args[0] != '':
            for i, elem in enumerate(args):
                if i == 0:
                    if args[0] != self.id:
                        super().id_update(self.id, args[i])
                setattr(self, attrs[i], elem)
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value != self.id:
                        super().id_update(self.id, value)
                setattr(self, key, value)

    def to_dictionary(self):
        "dictionary representation of a Square object"
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }