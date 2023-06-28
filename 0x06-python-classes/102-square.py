#!/usr/bin/python3
"""Class that defines a square"""

class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initializes a Square instance"""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.size ** 2

    def __eq__(self, other):
        """Equality comparator"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparator"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparator"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparator"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less than comparator"""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparator"""
        return self.area() <= other.area()
