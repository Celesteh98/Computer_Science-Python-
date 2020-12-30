# SpecialtyPizza.py
from Pizza import Pizza
from CustomPizza import CustomPizza

class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        super().__init__(size)
        self.name = name
        if self.size == "S":
            self.price = 12.00
        elif self.size == "M":
            self.price = 14.00
        elif self.size == "L":
            self.price = 16.00
        self.name = name

    def getPizzaDetails(self):
        specialtydetails = "SPECIALTY PIZZA\nSize: {}\nName: {}\nPrice: ${:.2f}\n".format(self.size, \
                  self.name, self.price)
        return specialtydetails
