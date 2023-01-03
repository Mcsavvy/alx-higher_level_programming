#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TextMaxInteger(unittest.TestCase):
    """
    A test case that contains tests against the
    function `max_integer` wthich finds and returns the
    maximum integer in a list
    """

    def test_empty_list(self):
        """
        test the `max_integer` function with an empty list.
        should return None
        """
        return_value = max_integer([])
        self.assertIs(return_value, None)

    def test_no_argument(self):
        """
        test the `max_integer` function with no arguments.
        should return None
        """
        return_value = max_integer()
        self.assertIs(return_value, None)

    def test_duplicate_max_value(self):
        """
        test the `max_integer` function with a list containing
        the max value twice.
        should return one of them
        """
        return_value = max_integer([1, 2, 2, 54, 34, 89, 89])
        self.assertEqual(return_value, 89)

    def test_max_value(self):
        """
        test the `max_integer` function with a list containing
        integers.
        should return the largest integer
        """
        return_value = max_integer([n ** 2 for n in range(20)])
        self.assertEqual(return_value, 19 ** 2)

        
