# Hangman

import random
score = 0
game = 0
while game == 0:

    HANGMAN = (
     """
      -------
      |      
      |
      |
      |
      |
      |
      |
      |
      -----------

     """ ,
     
     """

       -------
      |      |
      |
      |
      |
      |
      |
      |
      |
      -----------

     """ ,
     
     """

       -------
      |      |
      |      0
      |
      |
      |
      |
      |
      |
      -----------
      
     """ ,
     
     """

       -------
      |      |
      |      0
      |      +
      |
      |
      |
      |
      |
      -----------
            
     """ ,
     
     """

       -------
      |      |
      |      0
      |    /-+
      |
      |
      |
      |
      |
      -----------      
     """ ,
     
     """

       -------
      |      |
      |      0
      |    /-+-/
      |
      |
      |
      |
      |
      -----------

     """ ,
     
     """

       -------
      |      |
      |      0
      |    /-+-/
      |      |
      |     /
      |
      |
      |
      -----------

           """ ,
     
     """

       -------
      |      |
      |      0
      |    /-+-/
      |      |
      |     / /
      |
      |
      |
      -----------

      """)

    MAX_WRONG = 7

    WORDS = ("cheetah", "python","aardvark", "kangeroo",
          "gerbil", "sparrow", "jellyfish", "giraffe",
          "dormouse", "armadillo", "butterfly", "caribou",
          "caterpillar", "dolphin", "dragonfly", "ferret",
          "flamingo", "gazelle", "grasshopper", "hedgehog",
          "hummingbird", "koala", "locust", "llama", "magpie",
          "mole", "newt", "opossum", "panther", "pelican",
          "quail", "raccoon", "salamander", "scorpion",
          "tapir", "weasel", "woodpecker", "yak")

 # variables


    word = random.choice(WORDS)
    so_far = "-" * len(word)
    wrong = 0
    used = []

 
    print(
    """   WELCOME TO HANGMAN!

          You have 7 chances to
            guess the animal
         """ )

    
    while wrong < MAX_WRONG and so_far != word:
        print (HANGMAN[wrong])
        print(" You have guessed: ", used)
        print("\n So far, the word is:\n\n\n\t", so_far)
    
        guess = input("\n\n Enter your guess: ")
        guess = guess.lower()

        while guess in used:
            print("You've already guessed the letter", guess)
            guess = input("Enter your guess: ")
            guess = guess.lower()

        used.append(guess)

        if guess in word:
            print("\nYes! '", guess, "' is in the word!")
            wrong += 0
            print("You have", 7 - wrong, "chances left")
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new   
        else:
            print("Sorry, '", guess, "' isn't in the word")
            wrong+= 1
            print("You have", 7 - wrong, "chances left")
            
        
    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("\nYou've been hanged!")
        print("Your current score is: ", score)
    else:
        print("\nYou guessed it!")
        score += 1
        print("\nYour current score is: ", score)

    print("The word was", word)

    again = input("\nWould you like play again? (y,n): \n\n")
    if again == "n":
        print("Thanks for playing")
        game += 1
    
input("\nPress enter to exit")
          
