from LinkedList import LinkedList, Node

#Node tests

def test_NodeCreation():
    n = Node(20)
    assert n.getData() == 20
    assert n.getNext() == None

def test_NodeSetData():
    n = Node(20)
    n.setData(200)
    assert n.getData() == 200

def test_NodeSetNext():
    n =Node(20)
    n2 = Node(10)
    n.setNext(n2)
    assert n.getNext() == n2

#LinkedList Tests

def test_createList():
    ll = LinkedList()
    assert ll.isEmpty() == True

def test_addNodesToList():
    ll = LinkedList()
    ll.addToFront(10)
    ll.addToFront("Gaucho")
    ll.addToFront(False)
    assert ll.isEmpty() == False
    assert ll.length() == 3
    assert ll.search(10) == True
    assert ll.search("Gaucho") == True
    assert ll.search(False) == True
    assert ll.search("CS9") == False

def test_removeNodesFromList():
    ll = LinkedList()
    ll.addToFront(10)
    ll.addToFront("Gaucho")
    ll.addToFront(False)
    ll.addToFront("CS9")
    assert ll.length() == 4
    ll.remove(10)
    assert ll.search(10) == False
    assert ll.search("Gaucho") == True
    assert ll.search(False) == True
    assert ll.search("CS9") == True
    assert ll.length() == 3
    ll.remove(False)
    ll.search(False) == False
    ll.search("Gaucho") == True
    ll.search("CS9") == True
    assert ll.length() == 2
    assert ll.isempty() == False
    ll.remove("Gaucho")
    ll.remove("CS9")
    ll.isempty() == True
    ll.length() == 0

def test_insertIntoOrderedList():
    ll = LinkedList()
    ll.addToFront(50)
    ll.addToFront(40)
    ll.addToFront(30)
    ll.addToFront(20)
    ll.addToFront(10)
    ll.add(35)
    assert ll.getList() == "10 20 30 35 40 50"
    ll.add(5)
    assert ll.getList() == "5 10 20 30 35 40 50"
    ll.add(60)
    assert ll.getList() == "5 10 20 30 35 40 50 60"
