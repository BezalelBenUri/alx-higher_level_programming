import math
"""magical class"""


class MagicClass:
    """Class that replicates the given Python bytecode"""

    def __init__(self, radius=0):
        """Initialize MagicClass with radius"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the circle"""
        return 2 * math.pi * self.__radius
