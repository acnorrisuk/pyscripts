# pickling and shelving

import pickle, shelve

print("Shelving lists")
s = shelve.open("pickles2.dat")

s["bears"] = ["Jeremy", "Archie", "Mowgli"]
s["colours"] = ["red", "blue", "green"]
s["beers"] = ["Carlsberg", "Heineken", "Peroni"]

s.sync()
