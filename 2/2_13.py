#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

#Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum().

line = "Moj napis"
lista = line.split()
spacje = len(lista) - 1
ilosc_liter = len(line) - spacje
print(ilosc_liter)