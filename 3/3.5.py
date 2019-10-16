#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

#3.5
reply = raw_input("3.5\tPodaj dlugosc miarki: ")
try: 
    dlugosc = int(reply)
except ValueError:
    print "to nie jest liczba"
miarka = "|"
i=0
while i < dlugosc:
    miarka = miarka + "....|"
    i = i + 1
miarka = miarka + "\n0"
l = 1
while l <= dlugosc:
    if l < 10:
        miarka = miarka + "    " + str(l)
    elif 10 <= l < 100:
        miarka = miarka + "   " + str(l)
    else:
        miarka = miarka + "  " + str(l)
    l = l+1
print miarka