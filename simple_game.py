# importing modules

import games_mod, random

print("Welcome to the simplest game ever!")

again = None
while again != "n":
    players = []
    num = games_mod.ask_number(question = "how many players? (2-5): ", low = 2, high = 5)
    for i in range(num):
        name = input("Player name: ")
        score = random.randrange(100) + 1
        player = games_mod.Player(name, score)
        players.append(player)
        
    print("Results: ")
    for player in players:
        print(player)

    again = games_mod.ask_yes_no("Play again?: ")
    
        
input("exit")


