#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0         # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def count(self):      # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(N)
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.length == 0:
            raise ValueError("pusta lista")
        node = self.head
        self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        if self.length == 0:   # zabezpieczenie
            self.tail = None
        return node   # zwracamy usuwany node

    def remove_tail(self):   # klasy O(N)
        # Zwraca cały węzeł, skraca listę.
        # Dla pustej listy rzuca wyjątek ValueError.
        if self.length == 0:
            raise ValueError("Pusta lista")
        else:
            node = self.head
            if self.head == self.tail:
                to_remove = self.tail
                self.head = self.tail = None
                self.length = 0
                return to_remove
            else:
                while node.next != self.tail:
                    node = node.next
                to_remove = self.tail
                node.next = None
                self.tail = node
                self.length -= 1
                return to_remove

            
    def merge(self, other):    # klasy O(1)
        # Węzły z listy other są przepinane do listy self na jej koniec.
        self.tail.next = other.head
        self.tail = other.tail
        self.length += other.length
        other.clear()

    def clear(self):      # czyszczenie listy
        while self.head != self.tail:
            node = self.head
            self.head = self.head.next
            del node
        self.head = self.tail = None
        self.length = 0

# Zastosowanie.
alist = SingleList()
alist.insert_head(Node(11))         # [11]
alist.insert_head(Node(22))         # [22, 11]
alist.insert_tail(Node(33))         # [22, 11, 33]
blist = SingleList()
blist.insert_head(Node(44))         
blist.insert_head(Node(55))         
blist.insert_tail(Node(66))         # [55, 44, 66]
print ("length", alist.length)  # odczyt atrybutu
print ("length", alist.count()) # wykorzystujemy interfejs

alist.merge(blist)
print ("length", alist.length)  # odczyt atrybutu
print (blist.is_empty())
while not alist.is_empty():   # kolejność 22, 11, 33, 55, 44, 66
    print ("remove tail", alist.remove_tail().data)
print ("length", alist.length)  # odczyt atrybutu