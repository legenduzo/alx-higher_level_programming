#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for testing max_integer function"""

    def test_max_at_end(self):
        """Test with max integer at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with max integer at the beginning of the list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_negative(self):
        """Test with one negative integer in list"""
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)

    def test_all_negative(self):
        """Test will all negative numbers in list"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_only_one_number(self):
        """Test with list of same numbers"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
