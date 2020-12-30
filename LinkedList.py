'''
Linked Lists are a List structure that is not stored in coninuous memoru.
    * But this tructure still provides relative positiobing
    of the data in the Lists

Node: is an iterm in the LinkedList
    * A node usually contains the data we are storing in the list
    and a REFRENCE to the next node in the list.

Linked List object manages and maintains the chain of nodes as a collection
    * A Linked object contains HEAD refrence to the first node
    in this Linked List
    * methods in the LinkedList class should maintain the links
    between the nodes
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def addToFront(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        temp = self.head
        count = 0
        while temp != None:
            count = count + 1
            temp = temp.getNext()
        return count

    def search(self, item):
        temp = self.head
        found = False
        while temp != None and not found:
            if temp.getData() == item:
                found = True
            else:
                temp = temp.getNext()
            return found

    def remove(self, item):
        current = self.head

        if current == None: # empty list, do nothing
            return

        previous = None
        found = False
        while not found:
            if current == None:
                return
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
            # Case 1, 1st element
            if found == True and previous == None: 
                self.head = current.getNext()

            # Case 2, not 1st element
            if found == True and previous != None:
                previous.setNext(current.getNext())
        #Will work if items are in order
    def add(self, item):
        current = self.head
        previous = None
        stop = False

            # Find the correct place in the list.
        while current != None and not stop:
            if current.getData() > item:
                stop =True
            else:
                previous = current
                current = current.getNext()

                #Create Node with item to add
                temp = Node(item)

            #Case 1 insert at the front
            if previous == None:
                temp.setNext(self.head)
                self.head = temp

            #Case 2 insert not at front
            else:
                temp.setNext(current)
                previous.setNext(temp)

        # Method to get the items front to back
    def getList(self):
        current =self.head
        output = " "
        while current != None:
            output += str(current.getData()) + " "
            current = current.getNext()
        #remove the end space
        output = output [:len(output)-1]
        return output

'''
Ordered Liked List
* Similar to an unordered Linked List except the nodes in the list are ordered
with respect to each other.
* The implementation of both are similar, except we have to maintain the orderd
property of the nodes when we manage the list.
    *Most methods can be the same, but adding requires us to put a node in the
    correct position )instead of simplify just adding to the front of the List)
'''                
                    
'''
Sorting / Searching
* We've discucssed searching for things like
    * Linear search - start at the beginning and
    check every element in the List
        * Does not require elements to be sorted
        * O (log n)
    *But we haven't discussed HOW to sort lists
    * Many ways to do this, and some approaches are better then others
'''

''' Bubble Sort
Idea: ALgorith that will make severeal passes through the lsit and
swap adjacent elements to ensure the largest element end up at the end of the
list (assuming we're sorting in asscending (least to greatest) order).
'''
