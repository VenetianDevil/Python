#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from random import * 

# 11.1
# Przygotować moduł Pythona z funkcjami tworzącymi listy liczb całkowitych do sortowania. Przydatne są m.in. następujące rodzaje danych:
# (a) różne liczby int od 0 do N-1 w kolejności losowej,
# (b) różne liczby int od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji),
# (c) różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności,
# (d) N liczb float w kolejności losowej o rozkładzie gaussowskim,
# (e) N liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N).

def generate_rand(N):
    return sample(range(N), N)

def generate_almost_sorted(N):
    array = sample(range(N), N)
    number_to_shuffle = int(N/2)
    for i in range (0, number_to_shuffle):
        c = int(random() * N)
        temp = array[c]
        move = array[temp] 
        array[temp] = temp
        array[c] = move
    return array

def generate_reversed_sort(N):
    array = sample(range(N), N)
    array = sample(range(N), N)
    number_to_shuffle = int(N/2)
    for i in range (0, number_to_shuffle):
        c = int(random() * N)
        temp = array[c]
        move = array[N - temp - 1] 
        array[N - 1 - temp] = temp
        array[c] = move
    return array

def generate_gaussian(N, mu, sigma):
    array = [None] * N
    for i in range(0, N):
        array[i] = round(gauss(mu, sigma), 2)
    return array

def generate_repeted(N):
    array = [0] * N
    k = N - int(random()*N/2)
    for i in range(0, N):
        array[i] = int(random()*k)
    return array