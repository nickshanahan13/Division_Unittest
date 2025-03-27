#!/usr/bin/env python3

from divide import divide
import unittest

class TestDivide(unittest.TestCase):
    def test_basic(self):
        test_a = 8
        test_b = 2
        expected = 4
        self.assertEqual(divide(test_a, test_b), (expected))

unittest.main()