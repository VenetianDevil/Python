#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

#3.1 Czy podany kod jest poprawny składniowo w Pythonie?

    # sredniki w 1, 3, 5 linijce sa zbedne; nawiasy przy if też
    # for i in "qwerty": if ord(i) < 100: print i => blad dzialania przez zapis w jednej linijce
    # trzeba rozbic i zrobic wciecia
    # for i in "axby": print ord(i) if ord(i) < 100 else i => dziala okey

for i in "qwerty":
    if ord(i) < 100:
        print i
    # else: print "i>100"

#3.2 Co jest złego w kodzie:

    #L = [3, 5, 4] ; L = L.sort() => nie powinno byc przypisania sortu do L, tylko samo L.sort() wywolane
    #x, y = 1, 2, 3 => 3 jest nadmierna dana ktorej nie ma do czego przypisac
    #X = 1, 2, 3 ; X[1] = 4 => nie tworzymi listy, trzeba x przekonwertowac na Liste, zeby moc przypisac do X[1] 4
    #X = [1, 2, 3] ; X[3] = 4 => 3 element listy nie istnieje, tylko 0, 1, 2
    # X = "abc" ; X.append("d") => string nie posiada czegos takiego jak append()
    # map(pow, range(8)) => pow chce 2 argunentwo, a dostaje tylko po jednym z range(8)

#3.3
print ("3.3\t"),
for i in range(31):
    if i%3 != 0:
        print i,
print

#3.8
A = [1, 2, 5, 6, 9, 4, 5]
B = [3, 7, 7, 8, 6, 5, 2]
#a
C = []
for i in B:
    if i in A:
        C.append(i)
C = list(dict.fromkeys(C))
print "3.8a)\t" + str(C)
#b
D = A + B
D = list(dict.fromkeys(D))
print "3.8b)\t" + str(D)

#3.9
A =  [[],[4],(1,2),[3,4],(5,6,7)]
B = []
for i in A:
    suma = sum(i)
    B.append(suma)
print "3.9\t" + str(B)