#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unitttest.TestCase):
    """TestMaxInteger class for max_integer tests
    """

    def test_max_integer(self):
        """function to test max_integer
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEquals(max_integer([4, 1, 2, 3, 0]), 4)
        self.assertEqual(max_integer([1, 2, -4, 3, -5]), 3)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEquals(max_integer([]), None)
        with self.assertRaises(TypeError):
            max_integer("string")
            max_integer([1, 2, "string", 3, 4])
            max_integer([True])
            

if __name_ == '__main__':
    unittest.main()
