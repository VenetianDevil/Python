#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

#Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów w napisie. Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).

# rozbijanie ciagu wyrazow na elementy listy i sprawdzanie jej rozmiaru
line = "mam\t na imie\n kasia"
print(line)
a = line.split()
# wyrazy = len(a)
# print(a)
print(len(a)) #wypisanie ilosci wyrazow