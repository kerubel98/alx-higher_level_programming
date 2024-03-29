#!/usr/bin/python3
"""
Rectangle module definition
"""


class Rectangle:
    """
    Rectangel calss
    """

    number_of_instances = 0
    print_symbol = "#"

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
        ret = ""
        if self.__width == 0 or self.__height == 0:
            return ""
    
        for idx in range(self.__height):
            ret += str(self.print_symbol) * self.width
            if idx + 1 < self.__height:
                ret += '\n'
        return ret

    def __repr__(self):
        """return string rep"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """delete instance of rectangele"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ return rect with bigger area
        Args:
            rect_1 (Rectangle): Rectangle object
            rect_2 (Rectangle): Rectangle object
        Raises:
            Type error
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
