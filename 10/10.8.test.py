#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from randomqueue import *
import unittest

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = RandomQueue(5)

    def test__init__(self):
        self.assertEqual(self.queue.n, 6)

    def test_insert(self):
        self.queue.insert(3)
        self.assertEqual(self.queue.tail, 1)
        self.queue.insert(4) 
        self.queue.insert(6) 
        self.queue.insert(7)
        self.queue.insert(5)
        try:
            self.queue.insert(6)
        except ValueError:
            print "Kolejka przepelniona"

    def test_remove(self):  # zwraca losowy element
        try:
            self.queue.remove()
        except ValueError:
            print "Kolejka pusta"
        self.queue.insert(7)
        self.queue.insert(3)
        self.queue.insert(8)
        self.assertTrue(self.queue.remove() != None)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.insert(4)
        self.assertFalse(self.queue.is_empty())

    def test_is_full(self):
        self.assertFalse(self.queue.is_full())
        self.queue.insert(4)
        self.queue.insert(5)
        self.queue.insert(7)
        self.queue.insert(8)
        self.queue.insert(6)
        self.assertTrue(self.queue.is_full())

    def test_clear(self):     # czyszczenie listy
        self.queue.insert(5)
        self.queue.insert(7)
        self.assertFalse(self.queue.is_empty())
        self.queue.clear()
        self.assertTrue(self.queue.is_empty())
        

if __name__ == "__main__":
    unittest.main()     # wszystkie testy