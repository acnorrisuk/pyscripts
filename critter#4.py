#class attributes and non-static methods
import time

class Critter(object):
    """A virtual pet"""
    total = 0

    @staticmethod
    def status():
        print("\nTotal number of critters: ")

    def __init__(self, name):
        print("A new critter is born!")
        self.name = name
        Critter.total += 1

#main

print("Look out! Critters are on their way...")
time.sleep(2)
print("...")
time.sleep(2)
crit1 = Critter("critter 1")
time.sleep(2)
crit2 = Critter("critter 2")
time.sleep(2)
crit3 = Critter("critter 3")
time.sleep(2)
print("\n")
print(Critter.total)

Critter.status()

input("exit")
