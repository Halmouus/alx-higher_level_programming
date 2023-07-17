#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

fisrtrect = Rectangle(5, 5, 5, 5)
rect = Rectangle(10, 10, 10, 10)
print(rect)
rect.update(5)
print(rect)
rect.update(5, 4)
print(rect)
rect.update(5, 3)
print(rect)