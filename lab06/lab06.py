#lab06.py

from Apartment import Apartment

def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList)//2
        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i]< righthalf[j]:
                apartmentList[k]=lefthalf[i]
                i=i+1
            else:
                apartmentList[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            apartmentList[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            apartmentList[k]=righthalf[j]
            j=j+1
            k=k+1

def ensureSortedAscending(apartmentList):
    a = 0
    if len(apartmentList) <= 1:
        return True
    while a < len(apartmentList) - 1:
        if (apartmentList[a] < apartmentList[a+1]) or (apartmentList[a] == apartmentList[a+1]):
            a = a + 1
        else:
            return False
        return True

def getNthApartment(apartmentList, n):
    n = n -1
    if n in range(0, len(apartmentList)):
        return str(apartmentList[n].getApartmentDetails())
    else:
        return "(Apartment {}) DNE".format(n+1)

def getTopThreeApartments(sorted_apartmentList):
    if len(sorted_apartmentList) == 0 or len(sorted_apartmentList) == 1:
        return sorted_apartmentList
    if len(sorted_apartmentList) == 2:
        return "1st:{} 2nd:{}".format(sorted_apartmentList[0].getApartmentDetails(),sorted_apartmentList[1].getApartmentDetails())
    else:
        return "1st:{} 2nd:{} 3rd:{}".format(sorted_apartmentList[0].getApartmentDetails(),sorted_apartmentList[1].getApartmentDetails(), sorted_apartmentList[2].getApartmentDetails())

