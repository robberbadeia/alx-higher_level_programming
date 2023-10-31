#!/usr/bin/python3


"""_unitest_
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test Cases"""

    def test_one(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_two(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_three(self):
        self.assertEqual(max_integer([1, 2, 5, 4]), 5)

    def test_four(self):
        self.assertEqual(max_integer([-1, -2, -5, -4]), -1)

    def test_five(self):
        self.assertEqual(max_integer(['a', 'b', 'c', 'z']), 'z')


if __name__ == '__main__':
    unittest.main()
