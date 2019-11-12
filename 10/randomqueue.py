#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from random import random 

class RandomQueue:
    
    def __init__(self, size):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None] 
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def insert(self, data):
        if self.is_full():
            raise ValueError, "Przepelniona kolejka"
        else:
            self.items[self.tail] = data
            self.tail = (self.tail + 1) % self.n

    def remove(self):   # zwraca losowy element
        if self.is_empty():
            raise ValueError, "Kolejka pusta"
        else:
            index = int(random() * self.tail)
            node = self.items[index]
            while self.items[index] != None:
                self.items[index] = self.items[index+1]
                index = (index + 1) % self.n
            self.tail = (self.tail - 1) % self.n
            return node

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def clear(self):     # czyszczenie listy
        index = self.head
        while index != self.tail:
            self.items[index] = None
            index = (index + 1) % self.n
        self.tail = self.head

# queue = RandomQueue(5)
# queue.insert(1)
# queue.insert(2)
# queue.insert(3)
# queue.insert(4)
# queue.insert(5)
# # queue.insert(6) //wyrzuca wyjatek OK
# print queue.remove()
# print queue.remove()
# print queue.remove()
# print queue.remove()
# print queue.remove()
# # zwrocilo kazdy losowo OK
# # print queue.remove() //wyrzuca ze kolejka pusta OK