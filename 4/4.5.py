#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

#4.5
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print L
reply = raw_input("4.5\tPodaj (liczac od 0 do 9) 'left right': ")
reply.split()
try:
    left = int(reply[0])
    right = int(reply[2])
except ValueError:
    print "bledne dane"

# print str(left) + ' i ' + str(right)

# L[left:right+1] = reversed(L[left:right+1])
# print L

def odwracanie_iter(L, left, right):
    while left != right & left < right:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        left = left +1
        right = right - 1

odwracanie_iter(L, left, right)
print L

def odwracanie_rec(L, left, right):
    if left != right & left < right:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        odwracanie_rec(L, left+1, right-1)

odwracanie_rec(L, left, right)
print L