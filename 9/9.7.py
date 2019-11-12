#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, node):
        if self.data < node.data:      # na prawo
            if self.right:
                self.right.insert(node)
            else:
                self.right = node
        elif self.data > node.data:    # na lewo
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:
            pass    # ignoruję duplikaty

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return None


def bst_max(top):
    if top.data == None and top.left == None and top.right == None:
        raise ValueError, "Puste drzewo"
    else:
        while top.right != None:
            top = top.right
        return top

def bst_min(top):
    if top.data == None and top.left == None and top.right == None:
        raise ValueError, "Puste drzewo"
    else:
        while top.left != None:
            top = top.left
        return top

tree = Node()
try:
    print bst_max(tree)
except ValueError:
    print "Puste drzewo"
    
root = Node(3)
tree.insert(root)
tree.insert(Node(4))
tree.insert(Node(2))
tree.insert(Node(7))
tree.insert(Node(5))
tree.insert(Node(1))

print bst_max(root)
print bst_min(root)