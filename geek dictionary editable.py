# using dictionaries
# using pickle as save
# saved as dict1.dat

import pickle 

f = open("dict1.dat", "rb")
geek = pickle.load(f)
f.close()


choice = None

while choice != "0":
    print(
        """
       ~~~~~~~~~~~~~~~~~~~~~~~~~
       Geek Translator
       
       0 - Quit
       1 - Look up a geek term
       2 - Add a geek term
       3 - Redefine a geek term
       4 - Delete a geek term
       5 - Display all entries

       """
        )

    choice = input("Choice: ")
    print()

    keys = geek.keys()
    values = geek.values()
    items = geek.items()
    
# choice 0

    if choice == "0":
        print("goodbye")
        
# choice 1

    elif choice == "1":
        term = input("What do you want to translate?: ")
        term = term.upper()
        if term in geek:
            definition = geek[term]
            print("\n", term, ":", definition)
        else:
            print("\nSorry, I don't know!", term)

# choice 2

    elif choice == "2":
        term = input("What term would you like to add?: ")
        term = term.upper()
        if term not in geek:
            definition = input("What's the definition?: ")
            geek[term] = definition
            print("\n", term, "has been added to the dictionary")
        else:
            print("\n That term already exists! Choose 3 to redefine it")

# choice 3

    elif choice == "3":
        term = input("What term would you like to redefine?: ")
        term = term.upper()
        if term in geek:
            definition = input("What's the definition?: ")
            geek[term] = definition
            print("\n", term, "has been redefined")
        else:
            print("\nThat term doesn't exist")

# choice 4

    elif choice == "4":
        term = input("What term would you like to delete?: ")
        term = term.upper()
        if term in geek:
            del geek[term]
            print("\n", term, "has been deleted")
        else:
            print("\nThat term is not in the dictionary")

# choice 5

    elif choice == "5":
        print(keys)
        print("\nThere are",len(geek) ,"entries in the dictionary")
        
            
# unknown
    else:
        print("Sorry but", choice, "isn't a valid choice")

f = open("dict1.dat", "wb")
pickle.dump(geek, f)
f.close()

input("\n\nexit")
