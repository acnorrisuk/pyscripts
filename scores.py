# list methods

scores = []

choice = None

while choice != "0":
    print (
        """
 High Scores

 0 - Exit
 1 - Show score
 2 - Add a score
 3 - Delete a score
 4 - sort scores

 """
  )


    choice = input("choice: ")
    print()

#exit

if choice == "0":
    print("goodbye")

# show

elif choice == "1":
    print("Scores")
    for score in scores:
        print(score)

# add a score

elif choice == "2":
    score = int(input("What score did you get?: "))
    scores.append(score)

# remove

elif choice == "3":
    score = int(input("Remove which score?: "))
    if score in scores:
        scores.remove(score)
    else:
        print(score, "isn't in the high scores list")

# sort

elif choice == "4":
    scores.sort(reverse=True)
# error
    
else:
    print("Sorry, but", choice, "isn't a valid choice")

input("\n\nexit")
    
