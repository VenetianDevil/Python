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

n=100
k=10
i=0
y = int(random()*k)
L = create_List(n, k)
print (L)
print (y)
while i != None and i < n-1:
    i = linear_search(L, i+1, n-1, y)
    print (i)