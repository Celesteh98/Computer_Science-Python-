#BinarySearchTree.py

from TreeNode import TreeNode

class BinarySearchTree:
    def __init__(self):
        self.root = None # A BST just needs a refrence to the root node
        self.size = 0 # keeps track of number of nodes

    def length(self):
        return self.size

    def put(self, key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    #helper method to recursively walk down the tree
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = \
                TreeNode(key,val, parent = currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = \
                TreeNode(key,val, parent = currentNode)

    def get(self, key): # returns payload for key if it exists
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    # helper methof to recursivley walk down the tree
    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)


    def delete(self, key):
        if self.size >1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove) # remove modifies the tree
                self.size = self.size -1
            else:
                raise KeyError('Error, key not in tree')
            elif self.size == 1 and self.root.key == key:
                self.root = None
                self.size = self.size -1
            else:
                raise KeyError('Error, key not in tree')

    #used to remove the node and account for BST deletion cases
    def remove(self,currentNode):
        #case 1: node to remove is Leaf
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild None:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

        #case 3: Node to remove has both children
        elif currentNode.hasBothChildren():
            #Need to find the successor, remove successor, and replace
            #currentNode with successor's data / payload
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        #case 2: Node to remove has one child
        else:
            # Node has leftChild
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else: # currentNode is the root
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
        #Node has right child
        else:
            if currentNode.isLeftChild():
                currentNode.rightChild.parent = currentNode.parent
                currentNode.parent.leftChild = currentNode.rightChild
            elif currentNode.isRightChild():
                currentNode.rightChild.parent = currentNode.parent
                currentNode.parent.rightChild = currentNode.rightChild
            else:
                currentNode.replaceNodeData(currentNode.rightChild.key,
                                            currentNode.rightChild.payload,
                                            currentNode.rightChild.leftChild,
                                            currentNode.rightChild.rightChild)

    #used for pytesting
    def inOrder(self, node):
        ret=""
        if node != None:
            ret+= self.inOrder(node.leftChild)
            ret+= str(node.key) + ""
            ret+= self.inOrder(node.rightChild)
        return ret
    
