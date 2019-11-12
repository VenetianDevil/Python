#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from queue import *
import unittest

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(3)

    def test__init__(self):
        self.assertEqual(self.queue.n, 4 )      # utworzenie tablicy

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.put(4)
        self.assertFalse(self.queue.is_empty())

    def test_is_full(self):
        self.assertFalse(self.queue.is_full())
        self.queue.put(4)
        self.queue.put(5)
        self.queue.put(6)
        self.assertTrue(self.queue.is_full())

    def test_put(self):
        self.queue.put(3)
        self.assertEqual(self.queue.tail, 1)
        self.queue.put(4)
        self.queue.put(5)
        try:
            self.queue.put(6)
        except ValueError:
            print "Stos przepelniony"

    def test_get(self):
        try:
            self.queue.get()
        except ValueError:
            print "Stos pusty"
        self.queue.put(3)
        self.queue.put(4)
        self.assertEqual(self.queue.get(), 3)

if __name__ == "__main__":
    unittest.main()     # wszystkie testy