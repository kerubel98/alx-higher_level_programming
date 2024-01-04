#!/usr/bin/python3
"""rectangel class"""


class Rectangle:
    """Rectangel class """
    def __init__(self, width=0, height=0):

        """constractor

        Args:
            width
            height
        Raises:
            TypeError: if width or height not integer
            ValueError: if width or height less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """"width setter

        Args:
            value

        Raises:
            TypeError: if value not integer
            ValueError: if value less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Args:
            value

        Raise:
            TypeError:if value is not integer
            ValueError: if value is less zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value
