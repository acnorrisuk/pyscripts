# unpickling

import pickle, shelve

s = shelve.open("pickles2.dat")

print("Unshelving lists...")

print("beers -", s["beers"])
print("colours -", s["colours"])
print("bears -", s["bears"])

s.close()

input("exit")
