#test.file.py

from Animal import Animal
from AnimalShelter import AnimalShelter


def test____init__1():
    a = Animal("Cow", 190.0, 25,"Charlie")
    assert(a.species) == ("COW")
    assert(a.weight) == (190.0)
    assert(a.age) == (25)
    assert(a.name) == ("CHARLIE")


def test____init__2():
    a = Animal("Dog", 15.0, 7,"Cookie")
    assert(a.species) == ("DOG")
    assert(a.weight) == (15.0)
    assert(a.age) == (7)
    assert(a.name) == ("COOKIE")


def test____init__3():
    a = Animal("Rabbit", 22.0, 8,"Rabby")
    assert(a.species) == ("RABBIT")
    assert(a.weight) == (22.0)
    assert(a.age) == (8)
    assert(a.name) == ("RABBY")

def test__species__1():
    a = Animal("Cat", 15.0, 25,"Cater")
    a.setSpecies("CAT")
    assert(a.species)==("CAT")

def test__species__2():
    a = Animal("Fish", 2.0, 3,"Nemo")
    a.setSpecies("FISH")
    assert(a.species)==("FISH")

def test__species__3():
    a = Animal("Fish", 5.0, 8,"Dory")
    a.setSpecies("FISH")
    assert(a.species)==("FISH")

def test__weight__1():
    a = Animal("Squirrel", 12.0, 3,"Rena")
    a.setWeight(12.0)
    assert(a.weight)==(12.0)

def test__weight__2():
    a = Animal("Squirrel", 6.0, 1,"Roody")
    a.setWeight(12.0)
    assert(a.weight)==(12.0)

def test__weight__3():
    a = Animal("Squirrel", 12.0, 3,"Ron")
    a.setWeight(12.0)
    assert(a.weight)==(12.0)

def test__age__1():
    a = Animal("Sheep", 215.0, 5,"Shoosh")
    a.setAge(5)
    assert(a.age)==(5)

def test__age__2():
    a = Animal("Dog", 15.0, 6,"Woof")
    a.setAge(6)
    assert(a.age)==(6)

def test__age__3():
    a = Animal("Sheep", 275.0, 8,"Cloud")
    a.setAge(8)
    assert(a.age)==(8)

def test__name__1():
    a = Animal("Tiger", 515.0, 8,"Lilly")
    a.setName("LILLY")
    assert(a.name)==("LILLY")

def test__name__2():
    a = Animal("Tiger", 625.0, 10,"Larry")
    a.setName("LARRY")
    assert(a.name)==("LARRY")

def test__name__3():
    a = Animal("Bird", 5.0, 4,"Billie")
    a.setName("BILLIE")
    assert(a.name)==("BILLIE")

def test__toString__1():
    a = Animal("Horse", 1500.0, 5,"Amy")
    assert(a.toString()) == ("Species: HORSE, Name: AMY, Age: 5, Weight: 1500.0")

def test__toString__2():
    a = Animal("Crocodile", 7500.0, 5,"Cranky")
    assert(a.toString()) == ("Species: CROCODILE, Name: CRANKY, Age: 5, Weight: 7500.0")

def test__toString__3():
    a = Animal("Cheetah", 879.0, 12,"Chilly")
    assert(a.toString()) == ("Species: CHEETAH, Name: CHILLY, Age: 12, Weight: 879.0")

def test____init___1():
    a = Animal("Cheetah", 879.0, 12,"Chilly")
    b = AnimalShelter()
    assert(a.species) == ("CHEETAH")
    assert(a.weight) == (879.0)
    assert(a.age) == (12)
    assert(a.name) == ("CHILLY")

def test____init___2():
    a = Animal("Cat", 9.0, 2,"Catherine")
    b= AnimalShelter()
    assert(a.species) == ("CAT")
    assert(a.weight) == (9.0)
    assert(a.age) == (2)
    assert(a.name) == ("CATHERINE")

def test____init___3():
    a = Animal("Chicken", 39.0, 5,"Chicky")
    b= AnimalShelter()
    assert(a.species) == ("CHICKEN")
    assert(a.weight) == (39.0)
    assert(a.age) == (5)
    assert(a.name) == ("CHICKY")

def test__addAnimal__1():
    a = Animal("Chick", 10.0, 2,"Khloe")
    b= AnimalShelter()
    b.addAnimal(a)
    assert(b.AnimalShelter) == {"CHICK":[a]}

def test__addAnimal__2():
    a = Animal("Horse", 390.0, 15,"Kourtney")
    b= AnimalShelter()
    b.addAnimal(a)
    assert(b.AnimalShelter) == {"HORSE":[a]}

def test__addAnimal__3():
    a = Animal("Dinosaur", 3900.0, 50,"Kim")
    b= AnimalShelter()
    b.addAnimal(a)
    assert(b.AnimalShelter) =={"DINOSAUR":[a]}

def test__removeAnimal__1():
    a = Animal("Bird", 3.0, 50,"Kendall")
    b= AnimalShelter()
    b.addAnimal(a)
    b.removeAnimal(a)
    assert(b.AnimalShelter) =={"BIRD": []}

def test__removeAnimal__2():
    a = Animal("Bird", 3.0, 50,"Kendall")
    b= AnimalShelter()
    b.addAnimal(a)
    b.removeAnimal(a)
    assert(b.AnimalShelter) =={"BIRD": []}
def test_removeAnimal__3():
    a = Animal("Cow", 3.0, 50,"Kylie")
    b= AnimalShelter()
    b.addAnimal(a)
    b.removeAnimal(a)
    assert(b.AnimalShelter) =={"COW": []}

def test__getAnimalsBySpecies__1():
    a=Animal("Dog",12.0,7,"French")
    b= AnimalShelter()
    b.addAnimal(a)
    assert(b.getAnimalsBySpecies("Dog")) == ("Species: DOG, Name: FRENCH, Age: 7, Weight: 12.0")

def test__getAnimalsBySpecies__2():
    a=Animal("Cat",7.0,9,"Kris")
    b= AnimalShelter()
    b.addAnimal(a)
    assert(b.getAnimalsBySpecies("Cat")) ==("Species: CAT, Name: KRIS, Age: 9, Weight: 7.0")

def test__getAnimalsBySpecies__3():
    a=Animal("Lizard",6.0,3,"Cory")
    b= AnimalShelter()
    b.addAnimal(a)
    assert(b.getAnimalsBySpecies("Lizard")) == ("Species: LIZARD, Name: CORY, Age: 3, Weight: 6.0")

def test__doesAnimalExist__1():
    a=Animal("Mouse",5.0,7,"John")
    b= AnimalShelter()
    b.addAnimal(a)
    assert(b.doesAnimalExist(a)) == True

def test__doesAnimalExist__2():
    a=Animal("Rat",2.0,3,"Chris")
    b= AnimalShelter()
    b.addAnimal(a)
    assert(b.doesAnimalExist(a)) == True

def test__doesAnimalExist__3():
    a=Animal("Horse",1550.0,4,"Ariel")
    b= AnimalShelter()
    b.addAnimal(a)
    assert(b.doesAnimalExist(a)) == True




    



