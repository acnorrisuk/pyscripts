# creating and attributing of objects

class Critter(object):
    """A virtual pet"""
    def __init__(self, name):
        print("\nA new critter has been born!")
        self.name = name

    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name
        return rep

    def talk(self):
        print("Hewooh!")

#main

crit1 = Critter("Poochie")
print(crit1)
print(crit1.name)
crit1.talk()

crit2 = Critter("Moogle")
print(crit2)
print(crit2.name)
crit2.talk()

input("exit")
