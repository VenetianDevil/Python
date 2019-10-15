#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

#dane do zadan
from __future__ import print_function
line = "Tekst\tdo sprawdzania\nprogramow GvR"
print(line+"\n")
words = line.split()

#2.10 Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów w napisie. Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).
print("2.10\t" + str(len(words))) #wypisanie ilosci wyrazow

#2.11 Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.
word = "word"
print("2.11\t" + "_".join(word))

#2.12 Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.
print("2.12\t", end=''),
for i in words:
    print(i[0], end=''),
print()

#2.13 Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum().
spacje = len(words) - 1
ilosc_liter = len(line) - spacje
print("2.13\t" + str(ilosc_liter))

#2.14 Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.
longest = max(words)
print("2.14\ta) " + longest + " b) " + str(len(longest)))

#2.15 Na liście L znajdują się liczby całkowite dodatnie. Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.
L = [10, 4, 757, 34, 2, 732, 85]
print("2.15\t" + "".join(map(str,L)))

#2.16 W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum".
line = line.replace("GvR", "Guido van Rossum")
print("2.16\t" + line)

#2.17 Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości. Wskazówka: funkcja wbudowana sorted().
words.sort(key=str.lower)
print("2.17a)\t" + str(words))
words.sort(key = len)
print("2.17b)\t" + str(words))

#2.18 Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.
number = 1212300038200280
number = str(number)
print("2.18\t" + str(number.count("0")))

#2.19 Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().
numbers = (" ".join(map(str,L))).split()
for i,x in enumerate(numbers):
    numbers[i] = x.zfill(3) 
numbers = " ".join(numbers)
print("2.19\t" + str(numbers))