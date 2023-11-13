#!/usr/bin/python3
"""Rectangle Module

This module creates a rectangle.
It inherits from the Base class which manages id
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class

    Attributes:
        width (int): private - width of the rect
        height (int): private - height of rect
        x (int): private - point x
        y (int): private - point y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init method

        Args:
            width: positional argument
            height: positional argument
            x: keyword argument
            y: keyword argument
            id: keyword argument completed with super call
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """private getter and setter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 1:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @property
    def height(self):
        """private getter and setter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 1:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @property
    def x(self):
        """private getter and setter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @property
    def y(self):
        """private getter and setter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y
