# Critter full program

import time
import random

class Critter(object):
    """ A virtual pet """
    def __init__(self, name, hunger = random.randint(2, 3), boredom = random.randint(1, 2),
                 unloved = random.randint(1, 2), thirsty = random.randint(2, 3)):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.unloved = unloved
        self.thirsty = thirsty

# passtime

    def __pass_time(self):
        self.hunger += random.randint(1, 2)
        self.boredom += random.randint(0, 1)
        self.unloved += random.randint(0, 1)
        self.thirsty += random.randint(1, 2)

# mood

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom + self.unloved + self.thirsty
        if unhappiness <= 12:
            m = "happy"
            print(
    """
                   ()__()
                             
                   ( ^.^ )
                             
                   '(")(")'
  """ ) 
        elif 13 <= unhappiness <= 20:
            m = "okay"
            print(
    """
                    ()__()
                             
                    ( O.O )
                             
                    '(")(")'
  """ )
        elif 21 <= unhappiness <= 27:
            m = "frustrated"
            print(
    """
                    ()__()
                             
                    ( >.< )
                             
                    '(")(")'
  """ )
        elif 28 <= unhappiness <= 33:
            m = "tearful"
            print(
    """
                     ()__()
                             
                     (,o.o )
                             
                     '(")(")'
  """ )
        elif 33 <= unhappiness <= 41:
            m = "..."
            print(
    """
                     ()__()
                             
                     ( -.- )
                             
                     '(")(")'
  """ )
        else:
            m = "......"
        return m

# talk

    def talk(self):
        print("\t",self.name,": I feel", self.mood, "at the moment.\n")
        time.sleep(2)

# eat

    def eat(self, food = random.randint(5, 8)):
        print("\t"+self.name+": CRUNCH...")
        time.sleep(2)
        print("\t...")
        time.sleep(2)
        
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
            print("\n\t"+self.name+": Ugh! Full!")
        if self.hunger > 8:
            print("\n\t"+self.name+": I'm still hungry!")
        self.__pass_time()

# drink

    def drink(self, juice = random.randint(5, 8)):
        print("\t"+self.name+": SLURP...")
        time.sleep(2)
        print("\t...")
        time.sleep(2)
        burp_value = 2
        chance = random.randint(0, 2)
        if chance == burp_value:
            print("\n\t"+self.name+": Brruupp... Thank you!")
        if self.thirsty > 8:
            print("\n\t"+self.name+": I'm still thirsty!")
            
        self.thirsty -= juice
        if self.thirsty < 0:
            self.thirsty = 0
            print("\n\t"+self.name+": Ugh! No more!")
        self.__pass_time()
        

# love

    def love(self, hug = random.randint(4, 6)):
        print("\t*SQUEEZES YOU BACK*.")
        time.sleep(2)
        self.unloved -= hug
        if self.unloved > 8:
            print("\n\t"+self.name+": I need more hugs!")
        bliss_value = 0
        chance = random.randint(0, 2)
        if chance == bliss_value:
            print("\n\t"+self.name+": I Love you!")    
        if self.unloved < 0:
           self.unloved = 0
        self.__pass_time()

#play

    def play(self, fun = random.randint(4, 6)):
        print("\t*FLIES THROUGH THE AIR*")
        time.sleep(2)
        print("\n\t"+self.name+": Wheeeeee! SO MUCH FUN!")
        sick_value = 1
        chance = random.randint(0, 2)
        if chance == sick_value:
            print("\n\t"+self.name+": Urgh. Feel sick...")
        if self.boredom > 8:
            print("\n\t"+self.name+": I'm still bored!")
            
        time.sleep(2)
        self.boredom -= fun
        
        if self.boredom < 0:
            self.boredom = 0

        self.__pass_time()



print(
    """
          WELCOME TO THE CRITTER CARETAKER PROGRAM

           Please take good care of your critters
              Try to keep them feeling 'happy'
             """
    )
time.sleep(1)
input("Press enter to begin")
time.sleep(1)
print("\n\tYour egg is hatching!")
time.sleep(2)
print("\n\t...")
time.sleep(2)
print("\n\t...")
time.sleep(2)
print(
    """
                    ()__()
                              
                    ( 0.0 )

                    '(")(")'
  """ )
print("\nYou have a new critter!")
time.sleep(2)
crit_name = input("\nWhat name would you like to give your critter?: ")
crit_name = crit_name.upper()
crit = Critter(crit_name)
print("\nYour critter is now called...")
time.sleep(1)
print("\n\t"+crit.name)
time.sleep(2)

#main loop
    
def main():
    
    choice = None
    while choice != "0":
        print( 
            """
           ~~~
        0 - Sleep
        1 - Listen
        2 - Feed
        3 - Play 
        4 - Hug
        5 - Drink
        """ )
        choice = input("Choice: ")
        print()

        if crit.hunger > 12:
            print("\t"+crit.name+": I'm hungry!\n")
            
        if crit.thirsty > 12:
            print("\t"+crit.name+": I'm thirsty!\n")

        if crit.unloved > 12:
            print("\t"+crit.name+": I need love!\n")
            
        if crit.boredom > 12:
            print("\t"+crit.name+": I'm bored!\n")
            
        if crit.hunger + crit.boredom + crit.thirsty + crit.unloved > 33 < 41:
            print("\a")
            print("\tWARNING: "+crit.name+" needs help fast!\n")
        
        if crit.hunger + crit.boredom + crit.thirsty + crit.unloved > 42:
            choice = "0"
            print("\tSadly, "+crit.name+" is no more.")
            break

# choices

        if choice == "0":
            print("\t"+crit.name+":I  feel sleepy...")
            time.sleep(1)
            print("\n\t\tzzz.........")
            time.sleep(1)
            print("\t\t\tzzz......")
            time.sleep(1)
            print("\t\t\t\tzzz...")
            time.sleep(1)
            print("\n", crit.name," is now sound asleep")

        elif choice == "1":
            print(">>>")
            time.sleep(1)
            crit.talk()

        elif choice == "2":
            print(">>>")
            time.sleep(1)
            crit.eat()

        elif choice == "3":
            print(">>>")
            time.sleep(1)
            crit.play()

        elif choice == "4":
            print(">>>")
            time.sleep(1)
            crit.love()

        elif choice == "5":
            print(">>>")
            time.sleep(1)
            crit.drink()
            
        elif choice == "backdoor":
            print("\thunger:",crit.hunger, "\tboredom:",crit.boredom,
                  "\tunloved:", crit.unloved, "\n\n\tthirsty:", crit.thirsty, "\ttotal:",
                  crit.hunger + crit.boredom + crit.unloved + crit.thirsty, "\t mood: ",crit.mood)
            
        elif choice == "reset":
            crit.hunger = 0
            crit.boredom = 0
            crit.unloved = 0
            crit.thirsty = 0
            print("Parameters are reset")

        elif choice == "exit":
            break
            
        else:
            print("Sorry but" ,choice,"isn't a valid choice")
            main()

main()

input("\nPress enter to exit the program")

        
