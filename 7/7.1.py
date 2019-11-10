#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from fracs import *
import unittest

class TestFrac(unittest.TestCase):

    def setUp(self):
        self.zero = Frac(0, 2)
        self.frac1 = Frac(2, 5)
        self.frac2 = Frac(2, 5)
        self.x3y1 = Frac(3, 1)

    def test__init__(self):
        try:
            self.wrong = Frac(2, 0)
        except ValueError:
            print "create 2/0 catched"
        self.assertEqual(self.frac1.x, 2)
        self.assertEqual(self.frac1.y, 5)

    def test__str__(self):          # zwraca "x/y" lub "x" dla y=1
        self.assertEqual(self.frac1.__str__(), "2/5")
        self.assertEqual(self.x3y1.__str__(), "3")

    def test__repr__(self):       # zwraca "Frac(x, y)"
        self.assertEqual(self.frac1.__repr__(), "Frac(2, 5)")

    def test__cmp__(self):
        self.assertEqual(self.frac1.__cmp__(self.frac2), 0)
        self.assertEqual(self.frac1.__cmp__(self.zero), 1)
        self.assertEqual(self.frac1.__cmp__(self.x3y1), -1)

    def test__add__(self):
        self.assertEqual(self.frac1.__add__(self.frac2), Frac(4, 5))
        self.assertEqual(self.frac1.__add__(3), Frac(17, 5))

    def test__sub__(self):
        self.assertEqual(self.frac1.__sub__(self.frac2), 0)
        self.assertEqual(self.frac1.__sub__(3), Frac(-13, 5))

    def test__rsub__(self):     # int-frac
        self.assertEqual(self.frac1.__rsub__(3), Frac(13, 5))

    def test__mul__(self):
        self.assertEqual(self.frac1.__mul__(self.frac2), Frac(4, 25))
        self.assertEqual(self.frac1.__mul__(3), Frac(6, 5))

    def test__div__(self): 
        self.assertEqual(self.frac1.__div__(self.frac2), 1)
        self.assertEqual(self.frac1.__div__(3), Frac(2, 15))
        try:
            self.frac1.__div__(self.zero)       
        except ValueError:
            print "dividing by 0 catched"

    def test__rdiv__(self):
        self.assertEqual(self.frac1.__rdiv__(3), Frac(15, 2))
        try:
            self.zero.__rdiv__(4)       
        except ValueError:
            print "dividing by 0 catched"

    def test__pos__(self): # +frac = (+1)*frac
        self.assertEqual(self.frac1.__pos__(), self.frac1)

    def test__neg__(self):         # -frac = (-1)*frac
        self.assertEqual(self.frac1.__neg__(), Frac(-1*self.frac1.x, self.frac1.y))

    def test__invert__(self):      # odwrotnosc: ~frac
        self.assertEqual(self.frac1.__invert__(), Frac(self.frac1.y, self.frac1.x))

    def test__float__(self):      # float(frac)
        self.assertEqual(self.frac1.__float__(), 0.4)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy