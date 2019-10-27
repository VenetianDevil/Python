#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

#4.2
    #3.5
reply = raw_input("4.2 - 3.5\tPodaj dlugosc miarki: ")
try: 
    dlugosc = int(reply)
except ValueError:
    print "to nie jest liczba"

def func1(dlugosc):
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
    return miarka

print func1(dlugosc)

    #3.6
reply = raw_input("4.2 - 3.6\tPodaj 'axb': ")
reply.split()
try:
    x = int(reply[0])
    y = int(reply[2])
except ValueError:
    print "bledne dane"

def func2(x, y):
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
    return kratki

print func2(x, y)

#4.3
reply = raw_input("4.3\tPodaj n do silni: ")
try: 
    n = int(reply)
except ValueError:
    print "to nie jest liczba"

def factorial(n):
    s = i = 1
    while i <= n:
        s = s * i
        i=i+1
    return s

print str(n) + "! = " + str(factorial(n))

#4.4
reply = raw_input("4.4\tPodaj ktory wyraz ciagu fibonacciego obliczyc: ")
try: 
    n = int(reply)
except ValueError:
    print "to nie jest liczba"

def fibonacci(n):
    if n == 1 | n ==2:
        return 1
    else:
        a = 1
        b = 1
        i=3
        while i <= n:
            temp = a + b
            a = b
            b = temp
            i = i+1
    return b

print str(n) + "-ty wyraz ciagu to: "  + str(fibonacci(n))

#4.6
sequence = [(8, 1), 4, (6, [11, 12], (5, 6, (3, 1, 8)))]
print "4.6\t" + str(sequence)

def sum_seq(sequence):
    sum = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sum += sum_seq(item)
        else:
            sum += item
    return sum

print "suma liczb w sekwencji = " + str(sum_seq(sequence))

#4.7
seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print "4.7\t" + str(seq)
def flatten(seq):
    new_seq = []
    for item in seq:
        if isinstance(item, (list, tuple)):
            new_seq.extend(flatten(item))
        else:
            new_seq.append(item)
    return new_seq

print "sekwencja po spłaszczeniu: " + str(flatten(seq))
