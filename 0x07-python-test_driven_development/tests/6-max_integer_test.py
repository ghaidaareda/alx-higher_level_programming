#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_middle(self):
        self.assertEqual(max_integer([1,2,3,5,4]), 5)
    
    def test_max_beg(self):
        self.assertEqual(max_integer([6,2,3,5,4]), 6)

    def test_max_end(self):
        self.assertEqual(max_integer([1,2,3,5]), 5)

    if __name__ == '__main__':
        unittest.main()

