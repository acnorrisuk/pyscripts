import random

# create a sequence of words to choose from
WORDS = ("hello","goodbye","smile","evening","daytime")

#

# pick one word randomly from the sequence
word = random.choice(WORDS)

# create a variable to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print( \
"""
        Welcome to the anagram quiz!

   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
""")
print ("The jumble is:", jumble)

guess = input("\nYour guess: ")
guess = guess.lower()

while (guess != correct) and (guess != ""):
    print ("Sorry, that's not it.")
    guess = input("Your guess: ")
    guess = guess.lower()

if guess == correct:
    print ("That's it!  You guessed it!\n")

print ("Thank you for playing.")

input("\n\nPress the enter key to exit.")
