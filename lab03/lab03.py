# Lab03 Celeste Herrera

def removeSubString(str, sub):
    if (len(str) ==0):
        return ""
    if sub in str:
        return removeSubString(str.replace(sub,""), sub)
    else:
        return str

def reverseString(str):
    if len(str) == 0:
        return str
    else:
        return reverseString(str[1:]) + str[0]

def countInts(x, num):
    if not x:
        return 0
    if x[0]==num:
        return 1+countInts(x[1:],num)
    return countInts(x[1:],num)

def collectOddValues(odd):
    if not odd:
        return []
    if odd[0] % 2 == 1:
        return [odd[0]] + collectOddValues(odd[1:])
    return collectOddValues(odd[1:])

def multiply(a,b):
    if a < b:
        return multiply(b,a)
    elif b!=0:
        return (a + multiply(a, b-1))
    else:
        return 0
