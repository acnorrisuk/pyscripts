# pickling and shelving

import pickle, shelve

print("Pickling lists")
bears = ["Jeremy", "Archie", "Mowgli"]
colours = ["red", "blue", "green"]
beers = ["Carlsberg", "Heineken", "Peroni"]

f = open("pickles1.dat", "wb")

pickle.dump(bears, f)
pickle.dump(colours, f)
pickle.dump(beers, f)
f.close()
