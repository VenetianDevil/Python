#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

# Przeksztalcamy rownanie na rownanie prostej y = -(a/b)*x -c/b
# Rozwiazujemny dla x = 0 -> y = -c/b
# Rozwiazujemy dla y = 0 -> x = -c/a
# prosta idaca przez te dwa punkty na osi x i y zawiera roziwazania tego rownania

def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    x = -c / a
    y = -x / b
    OX = (x, 0)
    OY = (0, y)
    print "Pozwiązanie to prosta przechodzaca przez " + str(OX) + " i " + str(OY)
    
solve1(1, 2, 3)