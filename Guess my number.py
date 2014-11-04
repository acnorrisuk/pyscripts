# Guess number
# feedback

import random

print("\nI'm thinking of a number between 1 and 100")
print("See if you can guess it\n")

# variables

the_number = random.randint(1, 100)
guess = int(input("What is your guess?: "))
tries = 1

# guessing loop

while guess != the_number:
    if guess > the_number:
        print("Too high!")
    else:
        print("Too low!")

    guess = int(input("What is your guess?: "))
    tries +=1

print("\nYou are right! The number was", the_number)
print("\nIt only took you", tries, "tries!")

input("\n\nexit")
                

