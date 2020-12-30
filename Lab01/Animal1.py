#Animal.py

class Animal
    ''' Animal class type that contains attributes for all animals'''

    def __init__(self,species = None, name = None):
        self.species = species
        self.name = name

    def getAttributes(self):
        '''Returns a string representation of an Animal'''
        return '''Species; {}, Name: {}'''\
               .format(self.species,self.name)

    def getSounds(self):
        return "I'm an Animal!!!"

    
