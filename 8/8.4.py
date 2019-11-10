#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
import math

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if a + b < c or a + c < b or b + c < a:
        raise ValueError, "Niespelniony warunek trojkata"
    else:
        p = float( a + b + c ) / float(2)
        boki = (a, b, c)
        print "Pole trojkata " + str(boki) + " wynosi: "
        print math.sqrt(p * (p-a) * (p-b) * (p-c))

heron(3, 4, 5)
heron(1, 4, 4)
heron(1, 4, 6)
