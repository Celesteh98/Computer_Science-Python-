#AnimalShelter.py
from Animal import Animal

class AnimalShelter:
    def __init__(self):
        self.AnimalShelter = {}

    def addAnimal(self,animal):
        if self.AnimalShelter.get(animal.species) == None:
            self.AnimalShelter[animal.species] = [animal]
        elif not animal in self.AnimalShelter.get(animal.species):
            self.AnimalShelter[animal.species].append(animal)


    def removeAnimal(self,animal):
        if animal.species in self.AnimalShelter:
            if len(self.AnimalShelter[animal.species]) > 0:
                self.AnimalShelter[animal.species].remove(animal)
            else:
                print("No animal for species of type ", animal.species)


    def getAnimalsBySpecies(self,species):
        string = ""
        if self.AnimalShelter.get(species.upper()) == None:
            return string
        for a in self.AnimalShelter.get(species.upper()):
            string+= a.toString() + '\n'
        return string[:-1]
        
    def doesAnimalExist(self,animal):
        for item in self.AnimalShelter.keys():
            if  animal in  self.AnimalShelter[item]:
                return  True

        return  False

    def getShelter(self):
        return self.AnimalShelter
