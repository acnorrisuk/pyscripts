import random
tries = input("Press enter to flip the coin 100 times")

tries = 0
heads = 0
tails = 0
while tries < 100:
    tries += 1
    coin = random.randint(1, 2)
    if coin == 1:
        heads += 1
        print('Heads')
    if coin == 2:
        tails += 1
        print ('Tails')
total = tries

print("\nTotal coin flips: ", total,)
print("\nNo. of Heads: ", heads,)
print("\nNo. of Tails: ", tails,)

input ("\nenter")
