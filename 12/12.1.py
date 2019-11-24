#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from random import random

def linear_search(L, left, right, y):
    """Wyszukiwanie liniowe w ciągu."""
    i = left
    while i <= right:
        if y == L[i]:
            return i
        i += 1
    return None


def create_List(n, k):
    L = [None] * n
    for i in range(0, n):
        L[i] = int(random()*k)
    return L

L = create_List(100, 10)
print (linear_search(L, 0, 99, 5))