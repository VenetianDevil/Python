#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

# Przeksztalcamy rownanie na rownanie prostej y = -(a/b)*x -c/b
# Rozwiazujemny dla x = 0 -> y = -c/b
# Rozwiazujemy dla y = 0 -> x = -c/a
# prosta idaca przez te dwa punkty na osi x i y zawiera roziwazania tego rownania

def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    print (a, "x + ", b, "y + ", c, " = 0", "\tRozwiazanie to:")
    if a == 0 and b==0 and c!=0:
        raise ValueError("0 != ", c)
    if a == 0 and b != 0:
        y = -c / b
        print ("Zbior punktow, gdzie y = ", y)
    elif a != 0 and b == 0:
        x = -c /a
        print ("Zbior punktow, gdzie x = ", x)
    elif a != 0 and b != 0:
        if c == 0 and a == b:
            print ("Dwusieczna przechodzaca przez I i III cwiartke ukladu, x=y")
        elif c == 0:
            print ("Punkt (0,0)")
        else:
            x = -c / a
            y = -c / b
            OX = (x, 0)
            OY = (0, y)
            print ("Prosta przechodzaca przez", OX, " i ", OY)
    
solve1(1, 2, 3)
solve1(0, 2, 3)
solve1(1, 0, 3)
solve1(1, 0, 0)
solve1(1, 1, 0)
solve1(1, 2, 0)
solve1(0, 0, 1)
