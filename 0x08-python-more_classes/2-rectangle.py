#!/usr/bin/python3
"""2. Area and Perimeter"""


class Rectangle:
    """class for the Rectangle object"""
    def __init__(self, width=0, height=0):
        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = width
        else:
            raise TypeError("width must be an integer")
        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = height
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """returns the current rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the current rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @property
    def height(self):
        """property to retrieve the height"""
        return self.__height

    @property
    def width(self):
        """property to retrieve the width"""
        return self.width

    @width.setter
    def width(self, value):
        """property to set the width"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        """property to set the height"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")
