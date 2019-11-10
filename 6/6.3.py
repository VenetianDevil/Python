#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
# Kod testujący moduł.
from rectangles import * 
import unittest

class TestRectangle(unittest.TestCase):
    
    def setUp(self):
        self.rect = Rectangle(3, 4, 6, 8)
        self.rect_identical = Rectangle(3, 4, 6, 8)
        self.other = Rectangle(4, 3, 8, 6)

    def test___init__(self):
        self.assertEqual(self.rect.pt1, Point(3, 4))
        self.assertEqual(self.rect.pt2, Point(6, 8))

    def test___str__(self):         # "[(x1, y1), (x2, y2)]"
        self.assertEqual(self.rect.__str__(), "[(3, 4), (6, 8)]")

    def test___repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        self.assertEqual(self.rect.__repr__(), "Rectangle[(3, 4), (6, 8)]")

    def test___eq__(self):    # obsługa rect1 == rect2
        self.assertFalse(self.rect.__eq__(self.other))
        self.assertTrue(self.rect.__eq__(self.rect_identical))

    def test___ne__(self):       # obsługa rect1 != rect2
        self.assertTrue(self.rect.__ne__(self.other))
        self.assertFalse(self.rect.__ne__(self.rect_identical))

    def test_center(self):          # zwraca środek prostokąta
        self.assertEqual(self.rect.center(), Point(4.5, 6))

    def test_area(self):            # pole powierzchni
        self.assertEqual(self.rect.area(), 12)

    def test_move(self):      # przesunięcie o (x, y)
        self.rect.move(1, 2)
        ok_result = Rectangle(4, 6, 7, 10)
        self.assertTrue(self.rect.__eq__(ok_result))

if __name__ == "__main__":
    unittest.main()     # wszystkie testy