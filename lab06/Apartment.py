# Apartment.py Celeste Herrera

class Apartment:
    
    def __init__(self,rent= 0, metersFromUCSB= 0, condition= 0):
        self.rent = float(rent)
        self.metersFromUCSB = int(metersFromUCSB)
        self.condition = int(condition)

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return f"(Apartment) Rent: ${self.rent}," \
               f"Distance From UCSB: {self.metersFromUCSB}m," \
               f"Condition: {self.condition}/10"


    def __lt__(self, apartment):
        if self.rent == apartment.rent:
            if self.metersFromUCSB == apartment.metersFromUCSB:
                if self.condition > apartment.condition:
                    return True
                elif self.condition < apartment.condition:
                    return False
            elif self.metersFromUCSB < apartment.metersFromUCSB:
                return True
            elif self.metersFromUCSB > apartment.metersFromUCSB:
                return False
        else:
            if self.rent < apartment.rent:
                return True
            elif self.rent > apartment.rent:
                return False

    def __gt__(self, apartment):
        if self.rent == apartment.rent:
            if self.metersFromUCSB == apartment.metersFromUCSB:
                if self.condition < apartment.condition:
                    return True
                elif self.condition > apartment.condition:
                    return False
            if self.metersFromUCSB > apartment.metersFromUCSB:
                return True
            elif self.metersFromUCSB < apartment.metersFromUCSB:
                return False
        else:
            if self.rent > apartment.rent:
                return True
            elif self.rent < apartment.rent:
                return False

    def __eq__(self, apartment):
        return self.getApartmentDetails() == apartment.getApartmentDetails()

def test__eq__():
    a0 = Apartment(1204.56, 200, 3)
    a1 = Apartment(1204.56, 200, 3)
    assert (a0.getApartmentDetails() == a1.getApartmentDetails()) == True
    print(get.ApartmentDetails())
