''' Binary Search Tree
* BST Deletion
* We can break up deletion in three cases:
    Case 1: When the node to be deleted is a leaf node (no children)
    Case 2: When the node to be deleted has one child
    Case 3: When the node to be deleted has two children

Case 1: Case Delete a leaf node
* Find the node that needs to be deleted
* Simply remove the parent reference (either left child or right child)
to the deleted node

Case 2: Delete a node with one child
* Connect the deleted Node’s parent and the deleted Node’s child together

Case 3: Delete a node with two children
*First find the successor (node with next greater value) in the right subtree
    * This can be done by traversing the left children of the node
    to be deleted’s right subtree
    * Also note that the successor will always only have at most one child
        * If the successor had a left child, then it wouldn’t be the successor!
* Temporarily store the successor and delete the successor from the tree
    * Deleting the successor will fall in either Case 1 or Case 2
* Replace the deleted node’s value with the successor’s value
'''

#BinarySearchTree.py (continuing from last lecture)
from BinarySearchTree import BinarySearchTree

def test_deleteRoot():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(15, "fifteen")
    BST.put(5, "five")
    BST.put(3, "three")
    BST.put(7, "seven")
    BST.put(12, "twelve")
    BST.put(17, "seventeen")
    assert BST.inOrder(BST.root) == \
           "3 5 7 10 12 15 17"
    BST.delete(10)
    assert BST.inOrder(BST.root) == \
           "3 5 7 12 15 17"

def test_deleteLeafNode():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(15, "fifteen")
    BST.put(5, "five")
    BST.put(3, "three")
    BST.put(7, "seven")
    BST.put(12, "twelve")
    BST.put(17, "seventeen")
    BST.delete(3)
    assert BST.inOrder(BST.root) == \
        "5 7 10 12 15 17"
    BST.delete(17)
    assert BST.inOrder(BST.root) == \
           "5 7 10 12 15"

def test_deleteNodeWithTwoChildren():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(15, "fifteen")
    BST.put(5, "five")
    BST.put(3, "three")
    BST.put(7, "seven")
    BST.put(12, "twelve")
    BST.put(17, "seventeen")
    BST.delete(15)
    assert BST.inOrder(BST.root) == \
           "3 5 7 10 12 17"
    BST.delete(5)
    assert BST.inOrder(BST.root) == \
           "3 7 10 12 17"
        
    
    
    














