#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

if __name__ == "__main__":

    Rectangle.save_to_file([Rectangle(3, 4), Rectangle(5, 8, 1), Rectangle(9, 1, 3, 2)])
    with open("Rectangle.json", "r") as file:
        print(file.read())
    print(Rectangle.str_list())
    Rectangle.save_to_file([Rectangle(3, 4), Rectangle(5, 8, 1), Rectangle(9, 1, 3, 2)])
    with open("Rectangle.json", "r") as file:
        print(file.read())
    print(Rectangle.str_list())
    Square.save_to_file(None)
    with open("Square.json", "r") as file:
        print(file.read())
    print(Square.str_list())
    Square.save_to_file([])
    with open("Square.json", "r") as file:
        print(file.read())
    print(Square.str_list())
    Square.save_to_file([Square(2), Square(4, 1), Square(7, 3, 4)])
    with open("Square.json", "r") as file:
        print(file.read())
    print(Square.str_list())
    Square.save_to_file([Square(2), Square(4, 1), Square(7, 3, 4)])
    with open("Square.json", "r") as file:
        print(file.read())
    print(Square.str_list())