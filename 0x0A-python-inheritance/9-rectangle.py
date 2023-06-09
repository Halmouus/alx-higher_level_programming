#!/usr/bin/python3
"""Module that defines a class Rectangle
    that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation with width and height:
        width and height must be private. No getter or setter
        width and height must be positive integers, validated
        by integer_validator"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of a Rectangle object"""
        return self.__width * self.__height

    def __str__(self):
        """string format of a Rectangle object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
