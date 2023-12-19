#!/usr/bin/python3
"""Square clase"""


class Square:
    """Define Square class"""

    def __init__(self, size=0):
        """ constructor,

        Args:
            size: lenght of sides

        Rasises:
            TypeError: if size is not intiger
            ValueError: if size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """property getter

        Returns:
            size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """property setter

        Args:
            value

        Raises:
            TypeError: if size is not integer
            ValueError: if size < 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Area of a square

        Return:
            the size squared
        """
        return self.__size ** 2
