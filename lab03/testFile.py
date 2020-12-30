#testfile

from lab03 import multiply
from lab03 import collectOddValues
from lab03 import countInts
from lab03 import reverseString
from lab03 import removeSubString

def test_Multiply1():
    assert multiply(2,2) == 4

def test_Multiply2():
    assert multiply(9,9) == 81

def test_Multiply3():
    assert multiply(6,2) == 12

def test_Multiply4():
    assert multiply(5,2) == 10

def test_collectOddValues1():
    assert collectOddValues([1,2,3,4,5,6,7,8,9,10]) == [1,3,5,7,9]
    
def test_collectOddValues2():
    assert collectOddValues([3,2,3,2]) == [3,3]

def test_collectOddValues3():
    assert collectOddValues([10,11,12,13,14,15]) == [11,13,15]

def test_collectOddValues4():
    assert collectOddValues([5,2,1,4,3,7]) == [5,1,3,7]

def test_countInts1():
    assert countInts ([2,3,6,3,2,1], 2) == 2

def test_countInts2():
    assert countInts ([7,5,1,3,3,3,2], 3) == 3

def test_countInts3():
    assert countInts ([2,3,6,3,2,1], 2) == 2

def test_countInts4():
    assert countInts ([[], 3,5], 2) == 0

def test_reverseString1():
    assert reverseString("CMPSC9") == "9CSPMC"

def test_reverseString2():
    assert reverseString("DOG") == "GOD"

def test_reverseString3():
    assert reverseString("CAT") == "TAC"

def test_reverseString4():
    assert reverseString("COW") == "WOC"

def test_removeSubString1():
    assert removeSubString("Call","C") == "all"

def test_removeSubString2():
    assert removeSubString("Mother","Mot") == "her"

def test_removeSubString3():
    assert removeSubString("Celeste","este") == "Cel"

def test_removeSubString4():
    assert removeSubString("Telephone","Tele") == "phone"
