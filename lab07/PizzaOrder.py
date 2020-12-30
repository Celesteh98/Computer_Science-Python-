#PizzaOrder

from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder:
    def __init__(self, time):
        self.time = int(time)
        self.pizzas = []

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = int(time)

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        total = 0.0
        orderprinted = "******\n"
        orderprinted = orderprinted + "Order Time: {}\n".format(self.time)
        for c in self.pizzas:
            orderprinted= orderprinted + c.getPizzaDetails()
            orderprinted = orderprinted + "\n----\n"
            total = total + c.getPrice()
        orderprinted = orderprinted + "TOTAL ORDER PRICE: ${:.2f}\n".format(total)
        orderprinted = orderprinted + "******\n"
        return orderprinted

    def __gt__ (self, value):
        if self.time > value.time:
            return True
        else:
            return False

    def __lt__(self, value):
        if self.time < value.time:
            return True
        else:
            return False
