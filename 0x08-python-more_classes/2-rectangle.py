#!/usr/bin/python3
"""
Rectangle module definition
"""


class Rectangle:
    """
    Rectangel calss
    """
    def __init__(self, width=0, height=0):
        """
        constractor
        Args:
            width(int): width of rectangel
            height: height of rectangel
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        Args:
            value(int): width of rectangel
        raises:
            Type and value error
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        Args:
            value(int): height of rectangel
        Raises:
            type and value Error
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns: area of rectangel
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        restuens: permister of rectangel
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width + self.__height
