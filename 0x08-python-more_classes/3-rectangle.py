#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width

        Returns:
            int: Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width

        Args:
            value (int): Value to set the width

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height

        Returns:
            int: Height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height

        Args:
            value (int): Value to set the height

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Returns:
            int: The perimeter of the rectangle
        """
        return 2 * (self.__width + self.__height)
