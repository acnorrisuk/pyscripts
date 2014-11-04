# nesting

scores = []

choice = None
while choice != "0":

    print(
        """

     HIGH SCORES 2.0

     0 - Quit
     1 - List Score
     2 - Add a score
     """
        )
        

    choice = input("Choice : ")
    print()

    if choice == "0":
        print("Goodbye")
