#!/usr/bin/python3
"""class Rectangele that inhernt from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangel class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """intilaises Rectangel obj
        Args:
            width: privet instance attribut
            height: private instance attribut
            x: private instance attribute
            y: private inatnce attribute
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """overrides the __str__ method"""

        return ("[Rectangle]({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))
    
    def area(self):
        """Retuns area"""
        
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""

        rectw = ""
        spc = ""
        for x in range(self.__x):
            spc += " "
        for x in range(self.__width):
            rectw += "#"
        rectw = spc + rectw + "$"
        for x in range(self.__y):
            print("$")
        for x in range(self.__height):
            print(rectw)

    def update(self, *args, **kwargs):
        """Takes in multiple arguments and updates attributes
        Args:
            *args: multiple arguments
            **kwargs: dictionary arguments
        """
        attr = ["id", "width", "height", "x", "y"]
        for keys in range(len(args)):
            for atr in range(len(attr)):
                if atr == keys:
                    setattr(self, attr[atr], args[keys])
                    break
        if not args or len(args) == 0:
            for x in range(len(attr)):
                if attr[x] in kwargs:
                    setattr(self, attr[x], kwargs[attr[x]])


    @property
    def width(self):
        """Returns width as a private attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """Defines the width
        Args:
            value: integer that represents the width
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns height as a private attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """Defines the height
        Args:
            value: integer that represents the height
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns x as a private attribute"""

        return self.__x

    @x.setter
    def x(self, value):
        """Defines the x
        Args:
            value: integer that represents the x
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns y as a private attribute"""

        return self.__y

    @y.setter
    def y(self, value):
        """Defines the y
        Args:
            value: integer that represents the y
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
