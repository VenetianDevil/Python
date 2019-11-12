#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from stack import *
import unittest

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(3)

    def test__init__(self):
        self.assertEqual(self.stack.size, 3)      # utworzenie tablicy
        self.assertEqual(self.stack.n, 0)                      # liczba elementów na stosie

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(4)
        self.assertFalse(self.stack.is_empty())

    def test_is_full(self):
        self.assertFalse(self.stack.is_full())
        self.stack.push(4)
        self.stack.push(5)
        self.stack.push(6)
        self.assertTrue(self.stack.is_full())

    def test_push(self):
        self.stack.push(3)
        self.assertEqual(self.stack.n, 1)
        self.stack.push(4)
        self.stack.push(5)
        try:
            self.stack.push(6)
        except ValueError:
            print "Stos przepelniony"

    def test_pop(self):
        try:
            self.stack.pop()
        except ValueError:
            print "Stos pusty"
        self.stack.push(3)
        self.stack.push(4)
        self.assertEqual(self.stack.pop(), 4)

if __name__ == "__main__":
    unittest.main()     # wszystkie testy