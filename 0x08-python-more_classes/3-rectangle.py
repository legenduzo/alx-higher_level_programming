#!/usr/bin/python3
"""Rectangle Module

This module creates a rectangle object
"""


class Rectangle:
    """Rectangle class

    Creates a rectangle and provides it with attributes and methods

    Attributes:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes a new rectangle object

        Assigns values to attributes
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for self

        width must be greater than 0 and be an int
        """
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

    @property
    def height(self):
        """private property with getter and setter

        height must be greater than 0 and be an int
        """
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle

        If one side is 0, returns 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """A string representation of the rectangle instance

        Returns:
            strr (str): A string rectangle made up of # characters
        """
        strr = ''
        if self.width != 0 and self.height != 0:
            for i in range(0, self.height):
                strr += '#' * self.width
                if i != self.height - 1:
                    strr += '\n'
        return strr
