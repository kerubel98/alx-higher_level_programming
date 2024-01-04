#!/usr/bin/python3
"""
Rectangle module definition
"""


class Rectangle:
    """
    Rectangel calss
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        constractor
        Args:
            width(int): width of rectangel
            height: height of rectangel
        """
        Rectangle.number_of_instances += 1
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
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        printes "#" perimeter of rect
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        wid = ""
        lin = ""
        for i in range(self.__width):
            wid += "#"
        for i in range(self.height):
            lin += wid + "\n"
        return lin[:len(lin) - 1]

    def __repr__(self):
        """return string rep"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """delete instance of rectangele"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
