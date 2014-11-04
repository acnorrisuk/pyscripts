# global variables

def train():
    value = 200
    print("The train is travelling at", value, "km/h")

def walk():
    value = 5
    print("You are walking at",value, "km/h")

def world():
    value = 1675
    print("The world is spinning at", value, "km/h")

def space():
    value = 107372
    print("The world is travelling through space at", value, "km/h")


# total gets global value added

def total():
    print("In total, you are travelling at", value, "km/h")
    
# main

global value
value = 200 + 5 + 1675 + 107372

train()
walk()
world()
space()
total()

input("\nexit")

