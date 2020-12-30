# Fibonnaci
'''
* the nth number in the sequence is the sum of the
previous two numbers
* f(n) = f(n-1) + f(n-2)
f(0) = 0, f(1) = 1, f(2) = 1, f(3) = 2, f(4) = 3,...
'''

def fibonnaci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonnaci(n-1) + fibonnaci(n-2)
assert fibonnaci(0) == 0
assert fibonnaci(1) == 1
assert fibonnaci(2) == 2
assert fibonnaci(3) == 3
assert fibonnaci(4) == 4

def binarySearch(inList, item):
    if len(intList) == 0: # base case
        return False
    
    mid = len(intList) // 2
    if intList[mid] == item:
        return True
    elif item < intList[mid]:
        return binarySearch(intList[0:mid], item)
    else:
        return binarySearch(intList[mid+1:], item)

 def test_binarySearchNormal():
    assert binarySearch([1,2,3,4,5,6,7,8,9,10],5) == True
    assert binarySearch([1,2,3,4,5,6,7,8,9,10],0) == False
    assert binarySearch([1,2,3,4,5,6,7,8,9,10],11) == False
    assert binarySearch([1,2,3,4,5,6,7,8,9,10],1) == True
    assert binarySearch([1,2,3,4,5,6,7,8,9,10],10) == True

def test_binarySearchDuplicates():
    assert binarySearch([-10,-5,0,1,1,4,4,7,8],0) == True
    assert binarySearch([-10,-5,0,1,1,4,4,7,8],2) == False
    assert binarySearch([-10,-5,0,1,1,4,4,7,8],4) == True
    assert binarySearch([-10,-5,0,1,1,4,4,7,8],-5) == True

def test_binarySearchEmptyList():
    assert binarySearch([], 1): == False

def test_binarySearchSameValues():
    assert binarySearch ([5,5,5,5,5,5,5,5,5,5],5) == True
    assert binarySearch ([5,5,5,5,5,5,5,5,5,5],0) == False





    
'''
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

assert factorial(0) == 1
assert factorial(3) == 6
assert factorial(4) == 24

factorial(-1)

def double(n):
    return 2 * n

def triple(n):
    return n + double(n)

print(triple(5))
'''
