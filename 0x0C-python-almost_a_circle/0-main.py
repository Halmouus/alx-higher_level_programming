#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
    shape = Rectangle.create(**{ 'width': 2, 'height': 3 })
    print(shape)
    shape = Rectangle.create(**{ 'width': 2, 'height': 3, 'x': 12 })
    print(shape)
    shape = Rectangle.create(**{ 'width': 2, 'height': 3, 'x': 12, 'y': 1 })
    print(shape)
    shape = Rectangle.create(**{ 'width': 2, 'height': 3, 'x': 12, 'y': 1, 'id': 89 })
    print(shape)
    shape = Square.create(**{ 'size': 2 })
    print(shape)
    shape = Square.create(**{ 'size': 2, 'x': 1 })
    print(shape)
    shape = Square.create(**{ 'size': 2, 'x': 1, 'y': 3 })
    print(shape)
    shape = Square.create(**{ 'size': 2, 'x': 1, 'y': 3, 'id': 89 })
    print(shape)