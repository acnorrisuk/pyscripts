# tuples

# empty tuple

inventory = ()

# condition tuple

input("\nPress enter to see inventory")

# tuple with items

inventory = ("sword",
             "armour",
             "shield",
             "healing potion")

if not inventory:
    print("You are empty handed")
    

# for each element

print("\nYou are carrying: ")
for item in inventory:
    print(item)

print("\nYou have", len(inventory), "items in your possession")

drink = input("\ndrink healing potion? ")

if drink == "yes" or "yep" or "yeah":
    print("\nYour health is now replenished")
else:
    print("Your health is unaffected")

input("\nPress enter to continue\n")

# concatenate tuples

chest = ("gold", "gems")
print("You find a chest. it contains: ")
print(chest)
print("You add the contents to your inventory")
inventory += chest

input("\nPress enter to see inventory")

print("\nYou are carrying: ")
for item in inventory:
    print(item)

print("\nYou have", len(inventory), "items in your possession")

input("\nPress enter to continue")
