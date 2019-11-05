#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
import math 

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""
    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        point = (self.x, self.y)
        return str(point)

    def __repr__(self):        # zwraca string "Point(x, y)"
        point = (self.x, self.y)
        return "Point" + str(point)

    def __eq__(self, other):   # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        point = Point(self.x + other.x, self.y + other.y)
        return point

    def __sub__(self, other):  # v1 - v2
        point = Point(self.x - other.x, self.y - other.y)
        return point

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        # print (self.x * other.x) + (self.y * other.y)
        return (self.x * other.x) + (self.y * other.y)

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return math.sqrt((self.x * self.x) + (self.y * self.y))