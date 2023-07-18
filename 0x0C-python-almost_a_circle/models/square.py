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