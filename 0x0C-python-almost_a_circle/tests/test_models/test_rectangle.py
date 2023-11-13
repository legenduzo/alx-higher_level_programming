#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_initialization(self):
        rect = Rectangle(4, 5, 1, 2, 25)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 25)

    def test_width_property(self):
        rect = Rectangle(4, 5)
        rect.width = 10
        self.assertEqual(rect.width, 10)

    def test_height_property(self):
        rect = Rectangle(4, 5)
        rect.height = 10
        self.assertEqual(rect.height, 10)

    def test_x_property(self):
        rect = Rectangle(4, 5, 1, 2)
        rect.x = 3
        self.assertEqual(rect.x, 3)

    def test_y_property(self):
        rect = Rectangle(4, 5, 1, 2)
        rect.y = 4
        self.assertEqual(rect.y, 4)


if __name__ == '__main__':
    unittest.main()
