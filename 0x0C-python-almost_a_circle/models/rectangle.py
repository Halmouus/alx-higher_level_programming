#!/usr/bin/python3
"""2. First Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """class for the Rectangle object"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation with id, width, height, x and y"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """property to retrieve the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """property to set the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """property to retrieve the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """property to set the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """property to retrieve x"""

        return self.__x

    @x.setter
    def x(self, value):
        """property to set x"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """property to retrieve y"""

        return self.__y

    @y.setter
    def y(self, value):
        """property to set y"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        print(self.__y * "\n", end="")
        for i in range(self.__height):
            print(self.__x * ' ', end="")
            print(self.__width * '#')

    def __str__(self):
        "string representation of a Rectangle object"
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
                f" - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        "updates a Rectangle object"
        attrs = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0 and args[0] != '':
            for i, elem in enumerate(args):
                if i == 0:
                    if args[0] != self.id:
                        super().id_update(self.id, args[i])
                setattr(self, attrs[i], elem)
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value != self.id:
                        super().id_update(self.id, value)
                setattr(self, key, value)

    def to_dictionary(self):
        "dictionary representation of a Rectangle object"
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }