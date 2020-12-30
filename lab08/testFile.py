#testFile.py

from Card import Card
from PlayerHand import PlayerHand

#testing Card

def test___init__():
    x = Card('H', 'Q')
    assert x.suit == 'H'
    assert x.rank == 'Q'

def test___str__():
    x = Card('H', 'Q')
    assert x.__str__() == "H Q | 1\n"

def test___gt__():
    x = Card('H', 'Q')
    y = Card('H', '10')
    assert (x > y) == True
    c = Card('S', 'K')
    assert (x > c) == False
    d = Card('C', 'J')
    assert (x > d) == True

def test___lt__():
    x = Card('S', '8')
    y = Card('S', '10')
    assert (x < y) == True
    assert (y < x) == False
    c = Card ('S', '9')
    assert (x < c) == True
    d = Card('S', 'J')
    assert (x < d) == True

def test___eq__():
    g = Card('S', '5')
    h = Card('D', 'Q')
    assert (g == h) == False
    i = Card('S', '5')
    assert (h == i) == False
    assert (g == i) == True

#testing PlayerHand

def test_PlayerHand_functions():
    hand = PlayerHand()
    assert hand.root == None
    assert hand.isEmpty() == True
    hand.put('D', 'J')
    hand.put('D', 'K')
    assert hand.getTotalCards() == 2
    hand.put('S', 'J')
    hand.put('C', '3')
    hand.put('D', '5')
    hand.put('D', 'K')
    hand.put('D', 'K')
    assert hand.isEmpty() == False
    assert hand.getTotalCards() == 7
    hand.delete('D', 'J')
    hand.delete('D', 'K')
    hand.delete('C', '3')
    assert hand.getTotalCards() == 4
    assert hand.inOrder() == \
               "S J | 1\n\
                D 5 | 1\n\
                D K | 2"

    assert hand.getMin() ==  \
               "D 5 | 1\n"
    hand.put('D', '6')
    assert hand.getSuccessor('D', '5') == 'D 6 | 1\n'
    assert hand.get('S', 'J') == "S J | 1\n"
    assert hand.get('C', '10') == None
        
def test_PlayerHand_functions2():
    hand2 = PlayerHand()
    assert hand2.isEmpty() == True
    hand2.put('D', '5')
    hand2.put('H', 'A')
    hand2.put('D', 'Q')
    hand2.put('S', '6')
    assert hand2.preOrder() == \
               "D 5 | 1\n\
                H A | 1\n\
                D Q | 1\n\
                S 6 | 1\n"
    assert hand2.getTotalCards() == 4
    hand2.delete('D', '5')
    hand2.delete('H', 'A')
    hand2.delete('D', 'Q')
    hand2.delete('S', '6')
    assert hand2.getTotalCards() == 0
    assert hand2.getMin() == None
