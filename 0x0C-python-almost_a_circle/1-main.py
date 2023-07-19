#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

fisrtrect = Rectangle(5, 5, 5, 5)
rect = Rectangle(10, 10, 10, 10)
print(rect)
rect.update()
print(rect)
rect.update(5)
print(rect)
rect.update(5, 4)
print(rect)
rect.update(5, 3)
print(rect)
rect.update(550, 256, 128, 10, 20, y=8, id=35, width=36, x=4, height=23)
print(rect)