'''
# Pronounced “Deck”
* A Deque is a linear data structure that is more flexible
than a stack and a queue
    * A deque is also known as a “double-ended queue”
* A deque allows us to insert and remove from both ends
* Unlike a stack where we can only insert and remove from one end (top)
And a queue where we can insert in the front and remove from the end of a list
* Similar to a Stack and a Queue, we can implement Deques with a Python List
'''

class Deque:
    def __init__(self):
	self.items = []

    def isEmpty(self):
	return self.items == []

    def addFront(self, item):
	self.items.append(item)

    def addRear(self, item):
	self.items.insert(0, item)

    def removeFront(self):
	return self.items.pop()

    def removeRear(self):
	return self.items.pop(0)

    def size(self):
	return len(self.items)

# Pytests
def test_Deque():
    d = Deque()
    assert d.isEmpty() == True
    assert d.size() == 0
    d.addFront(10)
    d.addFront(20)
    d.addRear(30)
    d.addRear(40)
    assert d.isEmpty() == False
    assert d.size() == 4
    assert d.removeFront() == 20
    assert d.removeRear() == 40
    assert d.isEmpty() == False
    assert d.size() == 2
    assert d.removeRear() == 30
    assert d.removeRear() == 10
    assert d.isEmpty() == True
    assert d.size() == 0


'''
#Queue
# A Queue is linear data structure that has the First In, First
# Out (FIFO) property
# Analogy: Think about standing in line (no cutting!)
# Similar to a Stack, we can implement a Queue data structure
# using a Python List

class Queue:
    def __init__(self):
	self.items = []
	
    def isEmpty(self):
	return self.items == []

    def enqueue(self, item):
	self.items.insert(0, item)

    def dequeue(self):
	return self.items.pop()

    def size(self):
	return len(self.items)

# pytests
def test_insertIntoQueue():
	q = Queue()
	assert q.isEmpty() == True
	assert q.size() == 0
	q.enqueue("Customer 1")
	q.enqueue("Customer 2")
	assert q.isEmpty() == False
	assert q.size() == 2
    
def test_removeFromQueue():
	q = Queue()
	q.enqueue("Customer 1")
	q.enqueue("Customer 2")
	assert q.dequeue() == "Customer 1"
	assert q.isEmpty() == False
	assert q.size() == 1
	assert q.dequeue() == "Customer 2"
	assert q.isEmpty() == True
	assert q.size() == 0
'''

'''
# Stack Implementation

class Stack:
    def __init__(self):
	self.items = []
	
    def isEmpty(self):
	return self.items == []

    def push(self, item):
	self.items.append(item)

    def pop(self):
	return self.items.pop()

    def peek(self):
	return self.items[len(self.items)-1]

    def size(self):
	return len(self.items)

# Pytests
def test_insertIntoStack():
    s = Stack()
    assert s.isEmpty() == True
    s.push("There")
    s.push("Hi")
    assert s.size() == 2
    assert s.peek() == "Hi"
    assert s.isEmpty() == False
    assert s.peek() == "Hi"

def test_deleteFromStack():
    s = Stack()
    s.push("There")
    s.push("Hi")
    x = s.pop()
    assert x == "Hi"
    assert s.peek() == "There"
    assert s.size() == 1
    assert s.isEmpty() == False
    y = s.pop()
    assert y == "There"
    assert s.size() == 0
    assert s.isEmpty() == True
'''