#Animal.py
class Animal:
     '''Animal class type contains animals values
     Assume all animals have a specie, weight,age, name'''
    
     def __init__(self,species=None, weight=None, age=None, name=None):
          if type(species)== str:
               species = species.upper()
          if type(name)== str:
                name = name.upper()
          self.species = species
          self.weight = weight
          self.age = age
          self.name = name
         
     def setSpecies(self,species):
          if type(species)== str:
               species = species.upper()
          self.species = species
##         if species!= None:
##               species=species.upper()
##          else:
##               species=None
          
     def setWeight(self,weight):
          self.weight = weight

     def setAge(self,age):
          self.age = age

     def setName(self,name):
          if type(name)== str:
                name = name.upper()
          self.name = name
##          if name != None:
##               name=name.upper()
##          else:
##               self.species=None
##     
     def toString(self):
          return "Species: {0}, Name: {1}, Age: {2}, Weight: {3}".format(self.species,self.name,self.age,self.weight)




        
            
