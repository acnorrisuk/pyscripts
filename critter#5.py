#private variables and methods

class Critter(object):
    """ A Virtual Pet """
    def __init__(self, name, mood):
        print("A new critter has been born!")
        self.name = name              # public
        self.__mood = mood            # private

    def __private_method(self):
        print("This is private")

    def public_method(self):
        print("This is public")
        self.__private_method()

    def talk(self):
        print("\nI'm", self.name)
        print("Right now I feel", self.__mood, "\n")

#main

crit = Critter(name = "Poochie", mood = "happy")
crit.talk()
crit.public_method()

input("exit")
    
