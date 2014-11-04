# object interaction

class Player(object):
    """ Player """
    def blast(self, enemy):
        print("The player blasts an enemy.\n")
        enemy.die()

class Alien(object):
    """ Alien """
    def die(self):
        print("Ugh! ...")

#main

print("\tAlien death")

hero = Player()
invader = Alien()
hero.blast(invader)

input("exit")
