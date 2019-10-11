#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

#Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.

from __future__ import print_function

wyraz = "word"
print (wyraz[0], end=''),
for x in wyraz[1:]:
    print('_' + x, end=''),
    
print()