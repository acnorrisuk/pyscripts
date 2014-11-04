#Trivia
#takes input and reuses

name = input("Hi. What is your name? ")

age = int(input("What is you age? "))
weight = float(input("How many pounds do you weigh? "))

print("\nIf a small child were trying to get your attention they would say...\n")
print(name * 20)

seconds = age * 365 * 24 * 60 * 60
print("\nYou are now", seconds, "seconds old")

moon_weight = weight / 6
print("\nOn the moon you would weigh: ", moon_weight, "pounds")

sun_weight = weight * 27.1
print("\nOn the sun you would weigh: ", sun_weight, "pounds")

input("\n\n exit")
