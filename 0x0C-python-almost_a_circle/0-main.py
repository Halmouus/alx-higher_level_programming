#!/usr/bin/python3
""" 8-main """
from models.rectangle import Rectangle
from models.base import Base

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 3, 3, 15)
    r2 = Rectangle(10, 10, 10, 10, 89)
    print(r1)

    r1.update(19, height=1)
    print(r1)

    r1.update(width=1, wistrdssdsfdt=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=1)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)
    r1.update(550, 256, 128, 10, 20, y=8, id=35, width=36, x=4, height=23)
    print(r1)
    r2 = Rectangle(10, 10, 10, 10)
    print(Base.id_list())
    r2.update(551, id=44)
    r1.update(44)
    print(Base.id_list())