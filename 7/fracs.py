#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
import fractions

class Frac:
    """Klasa representujaca ulamki"""

    def __init__(self, x, y):
        # Sprawdzamy, czy y=0.
        if y==0:
            raise ValueError, "y=0"
        else:
            self.x = x
            self.y = y

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(self.x)
        else:
            return str(self.x) + "/" + str(self.y)

    def __repr__(self):        # zwraca "Frac(x, y)"
        frac = (self.x, self.y)
        return "Frac" + str(frac)

    def __cmp__(self, other):        # -1 | 0 | +1
        if type(other) == int:
            f2 = other
        else:
            f2 = float(other.x)/float(other.y)

        f1 = float(self.x)/float(self.y)
        if f1 < f2: 
            return -1
        elif f1 == f2:
            return 0
        else:
            return 1

    def __add__(self, other):        # frac + frac ; frac+int
        if type(other) == int:
            other = Frac(other, 1)
    
        if self.y == other.y:
            return Frac(self.x + other.x, self.y)
        else:
            NWD = fractions.gcd(self.y, other.y)
            mianownik = self.y * (other.y/NWD)
            licznik = (self.x * (other.y/NWD)) + (other.x * (self.y/NWD))
            NWD_skroc = fractions.gcd(licznik, mianownik)
            if mianownik/NWD_skroc == 1:
                return licznik/NWD_skroc
            else:
                return Frac(licznik/NWD_skroc, mianownik/NWD_skroc)

    __radd__ = __add__              # int+frac
 
    def __sub__(self, other):        # frac1-frac2, frac-int
        if type(other) == int:
            other = Frac(other, 1)

        if self.y == other.y:
            licznik = self.x - other.x
            NWD_skroc = fractions.gcd(licznik, self.y)
            return Frac(licznik/NWD_skroc, self.y/NWD_skroc)
        else:
            NWD = fractions.gcd(self.y, other.y)
            mianownik = self.y * (other.y/NWD)
            licznik = (self.x * (other.y/NWD)) - (other.x * (self.y/NWD))
            NWD_skroc = fractions.gcd(licznik, mianownik)
            if mianownik/NWD_skroc == 1 or licznik==0:
                return licznik/NWD_skroc
            else:
                return Frac(licznik/NWD_skroc, mianownik/NWD_skroc)

    def __rsub__(self, other):      # int-frac
            # tutaj self jest frac, a other jest int!
            return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):       # frac1*frac2, frac*int
        if type(other) == int:
            return Frac(self.x * other, self.y)
        elif self.x == 0 or other.x == 0:
            return 0
        else:
            licznik = self.x * other.x
            mianownik = self.y * other.y
            NWD_skroc = fractions.gcd(licznik, mianownik)
            if mianownik/NWD_skroc == 1:
                return licznik/NWD_skroc
            else:
                return Frac(licznik/NWD_skroc, mianownik/NWD_skroc)

    __rmul__ = __mul__              # int*frac

    def __div__(self, other):       # frac1/frac2, frac/int
        if type(other) == int:
            if other == 0:
                raise ValueError, "can't divide by 0"
            else:
                other=Frac(other, 1)
        elif other.x == 0:
            raise ValueError, "can't divide by 0"

        if(self.x == 0):
            return 0
        else:
            licznik = self.x * other.y
            mianownik = self.y * other.x
            NWD_skroc = fractions.gcd(licznik, mianownik)
            if mianownik/NWD_skroc == 1:
                return licznik/NWD_skroc
            else:
                return Frac(licznik/NWD_skroc, mianownik/NWD_skroc)

    def __rdiv__(self, other): # int/frac
        if self.x == 0:
            raise ValueError, "can't divide by 0"
        NWD_skroc = fractions.gcd(other * self.y, self.x)
        return Frac(other * self.y / NWD_skroc, self.x / NWD_skroc)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):          # -frac = (-1)*frac
        return Frac(-1 * self.x, self.y)

    def __invert__(self):      # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):       # float(frac)
        return float(self.x)/float(self.y)