#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 > x2 or y1 > y2:
            raise ValueError, "Zle wartości punktów"
        else:
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
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        if x1 > x2 or y1 > y2:
            raise ValueError, "Brak czesci wspolnej"
        else:
            wspolna = Rectangle(x1, y1, x2, y2)
            return wspolna
            
    def cover(self, other):    # prostąkąt nakrywający oba
        x1 = min(self.pt1.x, other.pt1.x)
        x2 = max(self.pt2.x, other.pt2.x)
        y1 = min(self.pt1.y, other.pt1.y)
        y2 = max(self.pt2.y, other.pt2.y)
        covering = Rectangle(x1, y1, x2, y2)
        return covering

    def make4(self):           # zwraca listę czterech mniejszych
        srodek = self.center()
        rtgl1 = Rectangle(self.pt1.x, srodek.y, srodek.x, self.pt2.y)
        rtgl2 = Rectangle(srodek.x, srodek.y, self.pt2.x, self.pt2.y)
        rtgl3 = Rectangle(self.pt1.x, self.pt1.y, srodek.x, srodek.y)
        rtgl4 = Rectangle(srodek.x, self.pt1.y, self.pt2.x, srodek.y)
        rtgls = [rtgl1, rtgl2, rtgl3, rtgl4]
        return rtgls