# constructors

class Critter(object):
    """ Virtual Pet"""
    def __init__(self):
        print("A new critter has been born!\n")


    def talk(self):
        print("Hewooh!\n")

#main

crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

input("exit")
              
              
