#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from generate import *
import subprocess
import os

def swap(L, left, right):
    """Zamiana miejscami dwóch elementów na liście."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item

# Wersja na podstawie Wróblewskiego.
def shakersort(L, left, right):
    count = 0
    k = right
    plik = open('sort.dat', 'w')
    write_to_file(plik, L)
    # os.system("gnuplot create.gnu")
    # count +=1
    while left < right:
        for j in range(right, left, -1):   # od prawej
            if L[j-1] > L[j]:
                swap(L, j-1, j)
                k = j
        left = k
        write_to_file(plik, L)
        # os.system("gnuplot create.gnu")
        # count +=1
        for j in range(left, right):   # od lewej
            if L[j] > L[j+1]:
                swap(L, j, j+1)
                k = j
        right = k
        write_to_file(plik, L)
        # count +=1
    plik.close()
    os.system("gnuplot create.gnu")

def write_to_file(plik, L):
    plik.write("\n")
    for i in range(0, len(L)):
        plik.write(str(i) + "\t" + str(L[i]) + "\n")
    plik.write("\n")

N = 100
# L = generate_gaussian(10, 3, 0.5)
# L = generate_repeted(N)
L = generate_rand(N)
shakersort(L, 0, N-1)