# Mood computer
# elif clause

import random

print("Welcome to the mood predictor")
print("You are...")

mood = random.randint(1, 3)

if mood == 1:
    #happy
    print( \

        """

   . .
  \___/

""" )


elif mood == 2:
    #neutral
    print( \
        """

   . .
   ___
  
 """ )

elif mood == 3:
    #sad
    print( \
        """
   . .

  /---\\

""")

else:
    print("You must be in a bad mood!")

input("exit")
