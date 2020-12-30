# testfile.py
from Apartment import Apartment
from lab06 import mergesort
from lab06 import ensureSortedAscending
from lab06 import getNthApartment
from lab06 import getTopThreeApartments

a0 = Apartment(1204.56, 200, 3)
a1 = Apartment(1204.56, 200, 7)
a2 = Apartment(1000, 100, 9)
a3 = Apartment(1000, 214, 10)
a4 = Apartment(300, 112, 3)
a5 = Apartment(300.52, 250, 2)

#test Apartment.py

def test___init__1():
    a0 = Apartment(1204.56, 200, 3)
    assert a0.rent == 1204.56
    assert a0.metersFromUCSB == 200
    assert a0.condition == 3

def test_getRent():
    assert a0.getRent() == 1204.56

def test_getMetersFromUCSB():
    assert a1.getMetersFromUCSB() == 200

def test_getCondition():
    assert a2.getCondition() == 9

def test_getApartmentDetails():
    assert a5.getApartmentDetails() == "(Apartment) Rent: $300.52, Distance From UCSB: 250m, Condition: 2/10,"

def test___gt__():
    assert (a1.getApartmentDetails() > a0.getApartmentDetails()) == True
    assert (a0.getApartmentDetails() > a1.getApartmentDetails()) == False

def test___lt__():
    assert (a0.getApartmentDetails() < a1.getApartmentDetails()) == True

def test___eq__():
    a0 = Apartment(1204.56, 200, 3)
    a1 = Apartment(1204.56, 200, 3)
    assert (a1.getApartmentDetails() == a0.getApartmentDetails()) == True

#test lab06.py

def test_mergesort():
    a0 = Apartment(1204.56, 200, 3)
    a1 = Apartment(1204.56, 400, 7)
    a2 = Apartment(1000, 100, 9)
    apartmentList = [a0, a1, a2]
    mergesort(apartmentList)
    assert apartmentList == [a2, a0, a1]

def test_ensureSortedAscending():
    a0 = Apartment(1204.56, 200, 3)
    a1 = Apartment(1204.56, 400, 7)
    a2 = Apartment(1000, 100, 9)
    apartmentList = [a0, a1, a2]
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True
    
def test_getNthApartment():
    a0 = Apartment(1204.56, 200, 3)
    a1 = Apartment(1204.56, 400, 7)
    a2 = Apartment(1000, 100, 9)
    apartmentList = [a0, a1, a2]
    mergesort(apartmentList)
    assert getNthApartment(apartmentList, 2) == a1


def test_getTopThreeApartments():
    a0 = Apartment(1204.56, 200, 3)
    a1 = Apartment(1204.56, 400, 7)
    a2 = Apartment(1000, 100, 9)
    a3 = Apartment(1000, 214, 10)
    a4 = Apartment(300, 112, 3)
    apartmentList = [a0, a1, a2, a3, a4]
    mergesort(apartmentList)
    assert apartmentList == [a4, a2, a3, a0, a1]
    assert getTopThreeApartments(apartmentList) ==  "1st:(Apartment) Rent: $300.00, Distance From UCSB: 112m, Condition: 3/10, 2nd:(Apartment) Rent: $1000.00, Distance From UCSB: 100m, Condition: 9/10, 3rd:(Apartment) Rent: $1000.00, Distance From UCSB: 214m, Condition: 10/10,"
'''
a0 = Apartment(1204.56, 200, 3)
a1 = Apartment(1204.56, 400, 7)
a2 = Apartment(1000, 100, 9)
a3 = Apartment(1000, 214, 10)
a4 = Apartment(300, 112, 3)
apartmentList = [a4, a2, a3, a0, a1]
mergesort(apartmentList)
print(getTopThreeApartments(apartmentList))
'''
