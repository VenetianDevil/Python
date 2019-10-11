#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

#Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.

from __future__ import print_function

line = "mam na imie Kara"
a = line.split()

for i in a:
    print(i[0], end=''),

print()