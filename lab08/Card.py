#Lab 08 Celeste Herrera
#card.py

class Card:
    def __init__(self, suit, rank):
        self.rank = rank.upper()
        self.suit = suit.upper()
        self.count = 1
        self.parent = None
        self.left = None
        self.right = None

    def getSuit(self):
        return self.suit

    def setSuit(self, suit):
        self.suit = suit

    def getRank(self):
        return self.rank

    def setRank(self, rank):
        self.rank = rank

    def getCount(self):
        return self.count

    def setCount(self, count):
        self.count = int(count)

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left  = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def __str__(self):
        return "{} {} | {}\n".format(self.suit, self.rank, self.count)           
        
    def __gt__(self, card):
        suits=['C','D','H','S']
        ranks=['A','2','3','4','5','6','7','8','9','10','J','Q','K']

        if ranks.index(self.rank)>ranks.index(card.rank):
            return True
        elif ranks.index(self.rank)<ranks.index(card.rank):
            return False
        else:
            if suits.index(self.suit)>suits.index(card.suit):
                return True
            else:
                return False

    def __lt__(self, card):
        suits= ['C','D','H','S']
        ranks= ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
       
        if ranks.index(self.rank)<ranks.index(card.rank):
            return True
        elif ranks.index(self.rank)>ranks.index(card.rank):
            return False
        else:
            if suits.index(self.suit)<suits.index(card.suit):
                return True
            else:
                return False
            
    def __eq__(self, card):
        if card == None:
            return False
        else:
            if (self.getRank() == card.getRank()) and (self.getSuit() == card.getSuit()):
                return True
            else: 
                return False

    def hasLeft(self):
        return self.left

    def hasRight(self):
        return self.right

    def isLeft(self):
        return self.parent and self.parent.left == self
    
    def isRight(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeft():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.hasAnyChildren():
            if self.hasLeft():
                if self.isLeft():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.isLeft():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent         
        
