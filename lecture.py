''' Priority Queues
* In a queue structure, we can insert items from the back the queue then remove
items from the back of the queue and remove items at the front of the queue
    * The order of elements in the queue were dictated by when items were
    inserted into the queue
*Priority Queues are similar to Queues EXCEPT:
    * We can insert items into the priority queue where an item has
    some value representing a priority, and items are ordered in the
    priority queue with respect to their priority value

A HEAP is COMPLETE binary tree
* A balanced binary tree: For any two leaf nodes, the difference of
depth is at most one
*Complete Tree: A binary tree where every level of the tree (except
the deepest) must contain as many nodes as possible. The deepest level
must have all nodes to the left as possible

Two types of Heap: MinHeap and MaxHeap

MaxHeap:
*A complete tree
*The value of a node is never less than the value of its children
 
MinHeap:
*A complete tree
*The value of a node is never greater than the value of its children

Heaps are an efficent way to implement a PRIORITY QUEUE
* The only element we care about when removing from the priority queue
is the root of the heap (the min value for a minHeap and the max value
for a maxHeap)

* Insertion order should not affect the strucure of the complete treee (since
operations need to preserve the complete balanced tree property)

* Since binary heaps have the complete property, we cab represent this with a
python List
    * easiest to represent the heap where the 0th index in the list is
    meangingless
    *The root of the binary heap is at index 1

*A node’s index with respect to its parent and children can be generalized as:
    * A node’s parent index: node_position // 2
    * A node’s left child index: 2 * node_position
    * A node’s right child index: 2 * node_position + 1

Insertion into a MaxHeap Steps
- insert the element in the first available location
    * Keeps the binary tree complete
- While the element’s parent is less than the element
    * Swap the element with its parent
- Insertion is O(log n) (height of tree is log n)



Removing Max (root) element in a MaxHeap Steps
*Since heaps are used to implement priority queues, removing
the root element is a commonly used operation
- Copy the root element into a variable
- Assign the last_element in the Python List to the root position
- While new root is less than one of its children
    * Swap the largest child with the last_element
- Return the original root element
- Deletion is O(log n) (height of tree is log n) 
'''

# MinHeap
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    #---insertion---
    def percUp(self,i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i//2
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
    # ----insertion----

    #---deletion---
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize -1
        self.heapList.pop()
        self.percDown(1)
        return retval
        #---deletion---

#pytest
def test_Binheap():
    bh = BinHeap()
    bh.insert(5)
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)
    assert bh.delMin() == 3
    assert bh.delMin() == 5
    assert bh.delMin() == 7
    assert bh.delMin() == 11
