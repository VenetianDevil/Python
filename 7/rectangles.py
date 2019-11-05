#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return "[" + self.pt1.__str__() + ", " + self.pt2.__str__() + "]"

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle[" + self.pt1.__str__() + ", " + self.pt2.__str__() + "]"

    def __eq__(self, other):   # obsługa rect1 == rect2
        return self.pt1.__eq__(other.pt1) and self.pt2.__eq__(other.pt2)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):          # zwraca środek prostokąta
        srodek = Point(float(self.pt1.x + self.pt2.x) / 2, float(self.pt1.y + self.pt2.y) /2)
        return srodek

    def area(self):            # pole powierzchni
        width = self.pt2.x - self.pt1.x
        hight = self.pt2.y - self.pt1.y
        return width * hight

    def move(self, x, y):      # przesunięcie o (x, y)
        self.pt1 = Point(self.pt1.x + x, self.pt1.y + y)
        self.pt2 = Point(self.pt2.x + x, self.pt2.y + y)

    def intersection(self, other): # część wspólna prostokątów
        # if self.pt1.x < other.pt1.x:
        #     left = self
        #     right = other
        # else:
        #     left = other
        #     right = self
        
        # if left.pt2.x < right.pt1.x:
        #     print 'rozlaczne prostokaty' #return 0
        # else:
            
    def cover(self, other): pass    # prostąkąt nakrywający oba

    def make4(self): pass           # zwraca listę czterech mniejszych