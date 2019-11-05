#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
# Kod testujący moduł.
from points import *
import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.point = Point(3, 4)
        self.other = Point(4, 4)
        self.point_identical = Point(3, 4)
    
    def test___init__(self):  # konstuktor
        self.assertEqual(self.point.x, 3)
        self.assertEqual(self.point.y, 4)

    def test___str__(self):         # zwraca string "(x, y)"
        self.assertEqual(self.point.__str__(), "(3, 4)")

    def test___repr__(self):        # zwraca string "Point(x, y)"
        self.assertEqual(self.point.__repr__(), "Point(3, 4)")

    def test___eq__(self):   # obsługa point1 == point2
        self.assertFalse(self.point.__eq__(self.other))
        self.assertTrue(self.point.__eq__(self.point_identical))

    def test___ne__(self):        # obsługa point1 != point2
        self.assertTrue(self.point.__ne__(self.other))
        self.assertFalse(self.point.__ne__(self.point_identical))
    
    # Punkty jako wektory 2D.
    def test___add__(self):  # v1 + v2
        ok_result = Point(7, 8)
        result = self.point.__add__(self.other)
        self.assertTrue(ok_result.__eq__(result))

    def test___sub__(self):  # v1 - v2
        ok_result = Point(-1, 0)
        result = self.point.__sub__(self.other)
        self.assertTrue(ok_result.__eq__(result))

    def test___mul__(self):  # v1 * v2, iloczyn skalarny
        self.assertEqual(self.point.__mul__(self.other), 28)

    def test_cross(self):         # v1 x v2, iloczyn wektorowy 2D
        self.assertEqual(self.point.cross(self.other), -4)

    def test_length(self):          # długość wektora
        self.assertEqual(self.point.length(), 5)

if __name__ == "__main__":
    unittest.main()     # wszystkie testy