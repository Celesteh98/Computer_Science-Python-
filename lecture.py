'''Quick SOrt
* Another divide and conquer algorithm
* Cna improve running times to O(n log n) in a typical case,
but we'll see that certain situations lead to )(n^2) on the worst case scenarios
* However, this performs BETTER than Merge sort since it does not need
additional space to sort elements
* Idea:
    * can sort a list by subdividing the list based oof of some PIVOT value
        *Please elements < pivot to the left side of the list
        *Please elements > pivot to the right side of the list
        * Recurse for each left / right portion of the list
        * we keep doing this until the sizes of each portion
        ==1 then the entire list is sorted
    * How do we partition the list into left / right sub lists?
    * Choose pivot (typically first element in list)
    *Find an element in the left side (using leftmark index)
    that’s out-of-place (> pivot)
    * Find an element in the right side (using rightmark index)
    that’s out-of-place (< pivot)
    * Swap out-of-place elements with each other
        - We’re putting them in the correct side of the list!
    * Continue doing steps 1 - 5 until the rightmark index < leftmark index
        -Swap the pivot with rightmark index
        -We’re putting the pivot element in the correct place!
''''




'''
MeregeSort

Idea: Divide and conquer algorithm
* Break a list into sublists where each sublist siza ==1
    * By definition, a list with one element is sorted!
* Merge each small sublist together to form a sorted larger list.
* Continue to merge these sublists back intot the original list
'''
def mergeSort(alist):
    if len(alist) > 1:
        mid= len(alist) // 2

        # uses additional space to create the left / right
        #halves
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        # recursivley sort the lefthalf, then the righthalf
        mergeSort(lefthalf)
        mergeSort(righthalf)

        
        # merge two sorted sublists (left / right halves)
        # into the original list (alist)
        i = 0 # index for lefthalf sublist
        j = 0 # index for righthalf sublist
        k = 0 # index for alist

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j  = j + 1
            k  = k + 1
        # put the remaining lefthalf elements (if any) into
	# alist
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        # put the remaining lefthalf elements (if any) into
	# alist
        while j < len(righthalf):
            alist[k] = lefthalf[j]
            j = j + 1
            k = k + 1
# pytest
def test_mergeSort():
   numList1 = [9,8,7,6,5,4,3,2,1]
   numList2 = [1,2,3,4,5,6,7,8,9]
   numList3 = []
   numList4 = [1,9,2,8,3,7,4,6,5]
   numList5 = [5,4,6,3,7,2,8,1,9]
   mergeSort(numList1)
   mergeSort(numList2)
   mergeSort(numList3)
   mergeSort(numList4)
   mergeSort(numList5)

   assert numList1 == [1,2,3,4,5,6,7,8,9]
   assert numList2 == [1,2,3,4,5,6,7,8,9]
   assert numList3 == []
   assert numList4 == [1,2,3,4,5,6,7,8,9]
   assert numList5 == [1,2,3,4,5,6,7,8,9]







