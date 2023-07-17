#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle
from models.base import Base

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    Base.id_list(Base)
    r2 = Rectangle(5, 5, 5, 5, 89)
    Base.id_list(Base)
    print("1", r1)
    print("2", r2)
    r2.update(0)
    print(r1)

    r1.update(99, 10)
    print(r1)
    print(r2)

    r1.update(45, 2, 3)
    print(r1)
    print(r2)

    r1.update(36, 2, 3, 10)
    print(r1)
    print(r2)

    r1.update(14, 2, 3, 4, 5)
    print(r1)
    print(r2)
    Base.id_list(Base)