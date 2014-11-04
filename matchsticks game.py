# matchsticks. start 20?
sticks = 21

print(
    """
              MATCHSTICKS GAME

              """
    )

print("\nThe game start with 21 matchsticks")
print("You can pick 1, 2 or 3 matches at a time")
print("Whoever picks the last one loses")

#pass 1

pick = int(input("\nHow many would you like to take? "))


    
    # put in breaking code when cheating

my_pick = 4 - pick

total = sticks - pick - my_pick

print("\nI take", my_pick, "matchsticks\n")

print(total, "matchsticks are left")



#pass 2

pick = int(input("\nHow many would you like to take? "))

my_pick = 4 - pick

totalb = total - pick - my_pick

print("\nI take", my_pick, "matchsticks\n")

print(totalb, "matchsticks are left")



#pass 3

pick = int(input("\nHow many would you like to take? "))

my_pick = 4 - pick

totalc = totalb - pick - my_pick

print("\nI take", my_pick, "matchsticks\n")

print(totalc, "matchsticks are left")


    
#pass 4

pick = int(input("\nHow many would you like to take? "))

my_pick = 4 - pick

totald = totalc - pick - my_pick

print("\nI take", my_pick, "matchsticks\n")

print(totald, "matchsticks are left")

    
#pass 5

pick = int(input("\nHow many would you like to take? "))

my_pick = 4 - pick

totale = totald - pick - my_pick

print("\nI take", my_pick, "matchsticks\n")

print(totale, "matchsticks are left")

if totale == 1:
    int(input("\nHow many would you like to take? "))
    print("\nThere are no matchsticks left")
    print("\nyou lose")

input("\nexit game")
    
