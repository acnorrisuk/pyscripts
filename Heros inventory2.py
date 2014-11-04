# lists


inventory = ["sword",
             "armour",
             "shield",
             "healing potion"]

if not inventory:
    print("You are empty handed")
    

print("\nYou are carrying: ")
for item in inventory:
    print(item)

print("\nYou have", len(inventory), "items in your possession")

input("\nPress enter to continue\n")

# indexing lists

index = int(input("\nEnter the index number for an inventory item: "))
print("At index", index, "is", inventory[index])

# slicing

start = int(input("\nEnter index number to begin slice: "))
finish = int(input("Enter index number to end slice: "))

print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])

input("\nPress enter to continue\n")

# concatenate two lists

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

# assign by index

print("You trade your sword for a crossbow")
inventory[0] = "crossbow"

input("\nPress enter to see inventory")

print("\nYou are carrying: ")
for item in inventory:
    print(item)

print("\nYou have", len(inventory), "items in your possession")

input("\nPress enter to continue")

