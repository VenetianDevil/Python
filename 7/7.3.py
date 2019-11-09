#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from rectangles import * 
import unittest

class TestRectangle(unittest.TestCase):
    
    def setUp(self):
        self.rect = Rectangle(3, 4, 6, 8)
        self.rect_identical = Rectangle(3, 4, 6, 8)
        self.other = Rectangle(4, 3, 8, 6)
        self.bez_pokrycia = Rectangle(7, 3, 8, 6)

    def test___init__(self):
        try:
            wrong = Rectangle(7, 3, 2, 1)
        except ValueError:
            print('wspolrzedne punktow sa niewlasciwe')

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

    def test_intersection(self): # część wspólna prostokątów
        ok_result = Rectangle(4, 4, 6, 6)
        wspl = self.rect.intersection(self.other)
        self.assertTrue(wspl.__eq__(ok_result))
        try:
            self.rect.intersection(self.bez_pokrycia)
        except ValueError:
            print 'Brak czesci Wspolnej'
            
    def test_cover(self):   # prostąkąt nakrywający oba
        ok_result = Rectangle(3, 3, 8, 8)
        cover = self.rect.cover(self.other)
        self.assertTrue(cover.__eq__(ok_result))

    def test_make4(self):
        rtgl1 = Rectangle(3, 6, 4.5, 8)
        rtgl2 = Rectangle(4.5, 6, 6, 8)
        rtgl3 = Rectangle(3, 4, 4.5, 6)
        rtgl4 = Rectangle(4.5, 4, 6, 6)
        rtgls = [rtgl1, rtgl2, rtgl3, rtgl4]
        self.assertEqual(self.rect.make4(), rtgls)    

if __name__ == "__main__":
    unittest.main()     # wszystkie testy