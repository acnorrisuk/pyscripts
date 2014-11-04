#jumble
count = 0

import random

WORDS = ("xylophone", "guitar", "bassoon", "piano",
         "violin", "clarinet", "ukelele", "flute", "harp",
         "saxophone", "banjo", "trombone", "recorder",
         "harmonica", "tuba", "bongos", "tambourine")

# random

word = random.choice(WORDS)

# variable

correct = word

# jumble word (prob below)

jumble =""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# game
print(
    """
          \n\t\tWORD JUMBLE

          """ )


print("\tWelcome to word jumble")
print("\tCan you unscramble the words?")
print("\tThey are all types of instruments\n")

input("\nPress enter to start ")
print("\nJUMBLE #1")

# jumble 1

print("\nThe jumble is:", jumble)

guess = input("\nYour guess: ")
if guess == correct:
    print("\nYou got it!")
    count += 1
else:
    print("\nSorry that's not right" *1)

input("Press enter to continue")

# next jumble
import random

WORDS = ("xylophone", "guitar", "bassoon", "piano", "violin", "clarinet", "ukelele")

# random

word = random.choice(WORDS)

# variable

correct = word

# jumble word 

jumble =""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# jumble 2

print("\nJUMBLE #2")  
print("\nThe jumble is:", jumble)


guess = input("\nYour guess: ")
if guess == correct:
    print("\nYou got it!")
    count += 1
else:
    print("\nSorry that's not right" *1)

input("Press enter to continue")

import random

WORDS = ("xylophone", "guitar", "bassoon", "piano", "violin", "clarinet", "ukelele")

# random

word = random.choice(WORDS)

# variable

correct = word

# jumble word

jumble =""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# jumble 3

print("\nJUMBLE #3")  
print("\nThe jumble is:", jumble)

guess = input("\nYour guess: ")
if guess == correct:
    print("\nYou got it!")
    count += 1
else:
    print("\nSorry that's not right" *1)
    
print("\n\tYou answered", count, "jumbles correctly!")
if count == 3:
    print("\tYou're a jumble master!")
elif count ==2:
    print("\tYou're a jumble junior!")
elif count ==1:
    print("\tYou're a jumble beginner!")
elif count ==0:
    print("\tYou're a jumble loser!")

input("\nPress enter to see your prize\n")
if count == 0:
    print("\tWhat, really?! You got 0 correct!")
elif count ==1:
    print("\tYou need 3/3 for a prize")
elif count ==2:
    print("\tYou need 3/3 for a prize")
elif count ==3: 
    print(
        """

           .''''.
          o|    |o
          o|    |o
          o|    |o
           ',__,'
            |  |
            |__|
            |  |
            |__|
            |  |
            |--|
            |__|
            |__|
            |--|
            |__|
            |__|
            |__|
            |__|
       . -  |__|  - .
      ' '   |__|   ' '
     '  '..'|__|'..'  '
     .                .
      '     8888     '
       '            '
       :    8888    :
      '     ____     '
     '     (____)     '
     :             o o :
     '.          o o .' 
       '-.,______,.-'  


      Gibson Gothic SG

"""
        )
    
input("\n\nPress enter to exit")




