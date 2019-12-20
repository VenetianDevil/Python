#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

def prime(n):
    if (n < 2):
        return False #is not
    
    i=2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print (prime(30))
print (prime(27))
print (prime(26))
print (prime(29))
print (prime(23))

def factorial(n):
    if n < 0:
        raise ValueError("non-negative integer required")
    s = i = 1
    while i <= n:
        s = s * i
        i=i+1
    return s

print (factorial(0))
print (factorial(3))
print (factorial(5))
# print (factorial(-1))

def greet(name):
    print ('Hello', name)

greet ('Karolina')