#TreeNode.py

class TreeNode:
    def __init__(self,key,val,left=None,right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        succ = None
        #Check if node has right subtree
        if self.hasRightChild():
            #traverse through left child (min)
            succ = self.rightChild.findMin()
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        #Case 1:
        #If node to be removed is a leaf, set parent's left or right child
        #refrences to None
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.LeftChild = None
            else:
                self.parent.rightChild = None

        #Case 2
        #Not a leaf node. should only have a right child for BST removal
        elif self.hasAnyChildren():
            if self.hasRightChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
#Note this code only goes through the findSucessor and spliceOut functionality
#necessary
#for BST matinence. There are more general cases that the textbook covers that
#you should read through and understand
                    
                    
                    
        
        
