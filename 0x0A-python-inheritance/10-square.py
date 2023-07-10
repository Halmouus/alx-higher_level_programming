#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

"""Module that defines a class Square
    that inherits from Rectangle"""


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation with szie:
        size must be private. No getter or setter
        size must be a positive integer, validated
        by integer_validator"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns area of a Square object"""
        return self.__size ** 2
