# properties

class Critter(object):
    """ A Virtual Pet """
    def __init__(self, name):
        print("A new critter has been born!")
        self.__name = name

    @property
    def name(self):
        return self.__name

    
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("A critter's name can't be an empty string")

        else:
            self.__name = new_name
            print("Name change successful. Your critter is now called: ", new_name)

    def talk(self):
        print("\nHi I'm", self.name)

#main

crit = Critter("Poochie")
crit.talk

print("\nMy critter's name is:", end= "")
print(crit.name)

print("\nChanging name...")
crit.name = "Randolph"
    
input("exit")
