#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from fracs import *
import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self): 
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self): 
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))

    def test_is_zero(self): 
        self.assertFalse(is_zero([1, 2]))
        self.assertTrue(is_zero([0, 2]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)
        self.assertEqual(cmp_frac([1, 2], [1, 2]), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy