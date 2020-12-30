

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

# helper function so we can pass in the first / last index
# of lists
def quickSortHelper(alist, first, last):
    if first < last:

    # will define the indices of the left / right sub lists
        splitpoint = partition(alist, first, last)

    # recursively sort the left / right sub lists
    quickSortHelper(alist, first, splitpoint-1) # left
    quickSortHelper(alist, splitpoint+1, last) # right

# partition function will organize left sublist < pivot
# and right sub list > pivot
def partition(alist, first, last):
    pivotvalue = alist[first] # choose first element as pivot

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        # move leftmark until we find a left element > pivot
	while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

	# move rightmark until we find a right element < pivot
	while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
	    rightmark = rightmark - 1

	# check if we're done swapping left / right elements in
	# correct side
	if rightmark < leftmark:
	    done = True
	else: # swap left and right elements into correct side of list
	    temp = alist[leftmark]
	    alist[leftmark] = alist[rightmark]
	    alist[rightmark] = temp
    # put the pivot value into the correct place (swap pivot w/ rightmark)
    temp = alist[first] # pivot
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

def test_quickSort():
   numList1 = [9,8,7,6,5,4,3,2,1]
   numList2 = [1,2,3,4,5,6,7,8,9]
   numList3 = []
   numList4 = [1,9,2,8,3,7,4,6,5]
   numList5 = [5,4,6,3,7,2,8,1,9]
   quickSort(numList1)
   quickSort(numList2)
   quickeSort(numList3)
   quickSort(numList4)
   quickSort(numList5)

   assert numList1 == [1,2,3,4,5,6,7,8,9]
   assert numList2 == [1,2,3,4,5,6,7,8,9]
   assert numList3 == []
   assert numList4 == [1,2,3,4,5,6,7,8,9]
   assert numList5 == [1,2,3,4,5,6,7,8,9]
