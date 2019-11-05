#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

#3.10
Slownik = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000} #pierwszy sposob
reply = raw_input("Podaj liczbe w rzymskich: ") [::-1]
# print reply
liczba = last = 0
for i in reply:
    if last > Slownik[i]:
        liczba = liczba - Slownik[i]
    else:
        liczba = liczba + Slownik[i]
    last = Slownik[i]
print "3.10\t liczba Arabska: " + str(liczba)