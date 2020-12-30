#testFile.py

from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue
from OrderQueue import QueueEmptyException 
import pytest

#Pizza tests

def test___init__():
    cp1 = CustomPizza("S")
    assert cp1.size == "S"


#Custom Pizza Tests

def test__init__2():
    cp2 = CustomPizza("M")
    assert cp2.size == "M"
    assert cp2.price == 10.00

def test_addTopping():
    cp2 = CustomPizza("M")
    assert cp2.price == 10.00
    cp2.addTopping("extra cheese")
    cp2.addTopping("pineapple")
    cp2.addTopping("sausage")
    assert cp2.price == 12.25

def test_getPizzaDetails():
    cp2 = CustomPizza("M")
    cp2.addTopping("extra cheese")
    cp2.addTopping("pineapple")
    cp2.addTopping("sausage")
    assert cp2.getPizzaDetails() == "CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ pineapple\n\
\t+ sausage\n\
Price: $12.25\n"

# testting Specialty Pizza

def test__init__3():
    cp3 = SpecialtyPizza("S", "Carne-more")
    assert cp3.size == "S"
    assert cp3.name == "Carne-more"

def test_getPizzaDetails_2():
    cp4 = SpecialtyPizza("S", "Carne-more")
    assert cp4.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"

# testing Pizza Order

def test__init__4():
    cp5 = PizzaOrder(0)
    assert cp5.time == 0

def test_addPizza():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) #12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)
    assert order.getOrderDescription() == \
"******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"

def test__gt__():
    ord1 = PizzaOrder(131423)
    ord2 = PizzaOrder(131427)
    assert (ord1 > ord2) == False

def test__lt__():
    ord3 = PizzaOrder(0)
    ord4 = PizzaOrder(225659)
    assert (ord3 < ord4) == True
    
# test Order Queue

def test_OrderQueue():
    queue = OrderQueue()
    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("M", "Carne-more")
    sp2 = SpecialtyPizza("S", "Veggie-Lover")
    order = PizzaOrder(123030)
    order.addPizza(cp1)
    order.addPizza(sp1)
    order.addPizza(sp2)

    queue.addOrder(order)
    assert queue.processNextOrder() == \
"******\n\
Order Time: 123030\n\
CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $14.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: M\n\
Name: Carne-more\n\
Price: $14.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Veggie-Lover\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $40.00\n\
******\n"
    with pytest.raises(QueueEmptyException):
        assert queue.processNextOrder()
