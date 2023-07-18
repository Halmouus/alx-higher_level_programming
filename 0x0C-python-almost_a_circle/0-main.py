#!/usr/bin/python3
""" 16-main """
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3)
    print(r1)
    r1 = Rectangle(2, 3)
    print(r1)
    Base.id_reset()
    r1 = Rectangle(2, 3)
    print(r1)
    r1 = Rectangle(2, 3)
    print(r1)