#PlayerHand.py

from Card import Card

class PlayerHand():
    def __init__(self):
        self.root = None
        self.size = 0

    def getTotalCards(self):
        return self.size

    def getMin(self):
        if self.size == 0:
            return None
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr

    def getSuccessor(self, suit, rank):
        if self.root:
            r = self._get(suit,rank,self.root)
            if r:
                if r.right:
                    r = r.right
                    while r.left:
                        r = r.left
                    return r
                else:
                    temp = r
                    while r:
                        if r > temp:
                            return r
                        r = r.parent
                    return None
            else:
                return None
        else:
            return None

    def _get(self, suit, rank, currentNode):
        dNode = Card(suit, rank)
        if not currentNode:
            return None
        elif dNode == currentNode:
            return currentNode
        elif dNode < currentNode:
            return self._get(suit, rank, currentNode.left)
        else:
            return self._get(suit, rank, currentNode.right)

    def put(self, suit, rank):
        if self.root:
           self._put(suit, rank, self.root)
        else:
            self.root = Card(suit, rank)
        self.size += 1

    def _put(self, suit, rank, currentNode):
        dNode = Card(suit,rank)
        if dNode < currentNode:
            if currentNode.left:
                self._put(suit,rank,currentNode.left)
            else:
                currentNode.left = dNode
                dNode.parent = currentNode
        elif dNode > currentNode:
            if currentNode.right:
                self._put(suit, rank, currentNode.right)
            else:
                currentNode.right= dNode
                dNode.parent = currentNode
        else:
            currentNode.count += 1

    def delete(self, suit, rank):
        n = Card(suit,rank)
        if self.size > 1:
            removeNode = self._get(suit, rank, self.root)
            if removeNode:
                self.remove(removeNode)
                self.size-=1
                return True
            else:
                return False
        elif self.size == 1 and n == self.root:
            self.root = None
            self.size -= 1
            return True
        else:
            return False

    def remove(self, n):
        if n.getCount() > 1:
            n.setCount(n.getCount()-1)
        elif (not n.left) and (not n.right):
            if n.parent.left:
                if n == n.parent.left:
                    n.parent.left = None
            if n.parent.right:
                if n == n.parent.right:
                    n.parent.right = None

        elif n.right and n.left: ## 2 children
            success = self.getSuccessor(n.suit,n.rank)
            success.spliceOut()
            n.suit = success.suit
            n.rank = success.rank
            n.count = success.count

        else: ## 1 child
            if n.left:
                if not n.parent:
                    n.left.parent = None
                    self.root = n.left
                else:
                    if n.parent.left:
                        if n.parent.left == n:
                            n.left.parent = n.parent
                            n.parent.left = n.left
                    if n.parent.right:
                        if n.parent.right == n:
                            n.left.parent = n.parent
                            n.parent.right = n.left

            else:
                if not n.parent:
                    n.right.parent = None
                    self.root = n.right
                else:
                    if n.parent.left:
                        if n.parent.left == n:
                            n.right.parent = n.parent
                            n.parent.left = n.right
                    if n.parent.right:
                        if n.parent.right == n:
                            n.right.parent = n.parent
                            n.parent.right = n.right

    def isEmpty(self):
        if self.root:
            return False
        else:
            return True
                
    def get(self, suit, rank):
        if self.root:
            r = self._get(suit, rank, self.root)
            if r:
                return r
            else:
                return None
        else:
            return None

    def inOrder(self):
        return self._inOrder(self.root)

    def _inOrder(self, n):
        returing = ''
        if n:
            returning += self._inOrder(n.left)
            returning += str(n)
            returning += self._inOrder(n.right)
        return returning

    def preOrder(self):
        return self._preOrder(self.root)

    def _preOrder(self,n):
        returning = ''
        if n:
            returning += str(n)
            returning += self._preOrder(n.left)
            returning += self._preOrder(n.right)
        return returning




