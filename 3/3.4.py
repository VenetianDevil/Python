#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

#3.4
print "3.4\t",
while True:
    reply = raw_input("Podaj liczbe rzeczywista: ")
    if reply == "stop":
        break
    try:
        number = int(reply)
    except ValueError:        # kod obsługujący błędy
        print "To nie jest liczba!"
    else:                     # jeśli nie było zgłoszenia wyjątku
        T = (number, pow(number, 3))
        print T