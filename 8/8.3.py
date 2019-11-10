#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from random import random
import math

def calc_pi(n):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    center = r = 10
    a = r * 2
    iterate = inside = outside = 0
    for i in range(0, n):
        # print i
        x = random() * a
        y = random() * a
        point = (x, y)
        # print str(point)
        length = math.sqrt(((x-center)*(x-center)) + ((y-center)*(y-center)))
        # print length
        if length < r:
            inside += 1
    
    pi = float(4*inside) / float(n)
    print "Dla " + str(n) + " losowan pi wynosi: " + str(pi)

calc_pi(20)
calc_pi(50)
calc_pi(100)
calc_pi(300)
calc_pi(500)
calc_pi(1000)
calc_pi(2000)