#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

#3.6
reply = raw_input("3.6\tPodaj 'axb': ")
reply.split()
try:
    x = int(reply[0])
    y = int(reply[2])
except ValueError:
    print "bledne dane"
kratki = "+"
i = 0
while i < x:
    kratki = kratki + "---+"
    i = i+1

dol = 0
while dol < y:
    kratki = kratki + "\n|"
    i = 0
    while i < x:
        kratki = kratki + "   |"
        i = i+1
    kratki = kratki + "\n+"
    i = 0
    while i < x:
        kratki = kratki + "---+"
        i = i + 1
    dol = dol + 1
print kratki