# unpickling

import pickle, shelve

print("Unpickling lists...")

f = open("pickles1.dat", "rb")
bears = pickle.load(f)
colours = pickle.load(f)
beers = pickle.load(f)

print(bears)
print(colours)
print(beers)

f.close()

input("exit")
