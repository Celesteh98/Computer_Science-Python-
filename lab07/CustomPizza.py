#CustomPizza.py

from Pizza import Pizza

class CustomPizza(Pizza):

    def __init__(self, size):
        super().__init__(size)
        self.toppings = []
        if self.size == "S":
            self.price = 8.00
        elif self.size == "M":
            self.price = 10.00
        elif self.size == "L":
            self.price = 12.00

    def addTopping(self, topping):
        self.toppings.append(topping)
        if self.size == "S":
            self.price = self.price + 0.50
        elif self.size == "M":
            self.price = self.price + 0.75
        elif self.size == "L":
            self.price = self.price + 1.00

    def getPizzaDetails(self):
        customdetails = "CUSTOM PIZZA\nSize: {}\nToppings:".format(self.size)
        if self.toppings != []:
            for i in self.toppings:
                customdetails = customdetails + "\n\t+ {}".format(i)
        customdetails = customdetails + "\nPrice: ${:.2f}\n".format(self.price)
        return customdetails
