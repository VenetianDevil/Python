#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from random import random

def bin_search(L, l, r, y):
    """Wyszukiwanie binarne w wersji rekurencyjnej."""
    middle = int((l+r)/2)
    # print (middle)
    if( L[middle] == y):
        return middle
    elif (l>r):
        raise ValueError("List don't contain wanted value")
    elif (L[middle] > y):
        return bin_search(L, l, middle-1, y)
    else:
        return bin_search(L, middle+1, r, y)

L = [1, 2, 5, 8, 9, 11, 15, 20]
print (bin_search(L, 0, 7, 5))