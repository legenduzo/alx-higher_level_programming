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
        number_of_instances (int): defined
        print_symbol (any): symbol to print when str(Rectangle) is called
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0, print_symbol=None):
        """Initializes a new rectangle object

        Assigns values to attributes
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = (print_symbol
                             if print_symbol
                             else Rectangle.print_symbol)

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
            symbol = str(self.print_symbol)
            strr = '\n'.join([symbol * self.width for _ in range(self.height)])
        return strr

    def __repr__(self):
        """Implements repr for the rectangle class

        Return:
            str: String representation of rectangle attributes
        """
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Prints a message that communicates deletion"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the greater area. It returns
        rect_1 if both rectangles have the same area.

        Parameters:
            rect_1 (Rectangle): The first rectangle
            rect_2 (Rectangle): The second rectangle

        Returns:
            Rectangle: The rectangle with the greater area, or rect_1 if
              both rectangles have the same area.

        Raises:
            TypeError: If either rect_1 or rect_2 are not of type Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
