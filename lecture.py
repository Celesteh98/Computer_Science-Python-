'''
Binary Search Tree (BST)
Recall that a binary tree is a tree structure where a node may have at most two children
    * Binary Search Trees (BST) are binary trees that have the following
    property:
    * Values that are less than the parent are found in the left subtree
    * Values that are greater than the parent are found in the right subtree
    * This is known as the BST property
* Binary Search Trees are also one way to implement a Map Abstract Data Type
    * A Map ADT maps keys to corresponding values
    * Think of keys defining where in the BST structure a node gets inserted
And each node has a corresponding value field
Similar to how Python Dictionaries work on a high-level (but the underlying implementation between a Python Dictionary and BST are different (each with pros / cons))
Example: Inserting the following keys into a BST
''''

from BinarySearchTree import BinarySearchTree

def test_insertRoot():
    BST = BinarySearchTree()
    assert BST.root == None
    assert BST.length() == 0

def test_insertRoot():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    assert BST.root.key == 10
    assert BST.root.payload == "ten"
    assert BST.root.hasLeftChild() == None
    assert BST.root.hasRightChild() == None
    assert BST.root.isLeftChild() == None
    assert BST.root.isRightChild() == None
    assert BST.root.isRoot() == True
    assert BST.root.hasAnyChildren() == None
    assert BST.root.isLeaf() == True
    assert BST.root.hasBothChildren() == None
    assert BST.root.replaceNodeData(20, "twenty" ,None, None)
    assert BST.root.key == 20
    assert BST.root.payload == "twenty"

def test_insertNodes():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(20, "twenty")
    BST.put(15, "fifteen")
    BST.put(5, "five")
    assert BST.root.key == 10
    assert BST.root.leftChild.key == 5
    assert BST.root.rightChild.key == 20
    assert BST.root.rightChild.leftChild.key == 15

def test_get():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(20, "twenty")
    BST.put(15, "fifteen")
    BST.put(5, "five")
    assert BST.get(10) == "ten"
    assert BST.get(20) == "twenty"
    assert BST.get(15) == "fifteen"
    assert BST.get(5) == "five"
    assert BST.get(30) == None
            
