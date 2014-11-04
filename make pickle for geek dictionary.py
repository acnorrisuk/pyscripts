# writing dictionary
import pickle, shelve

print("Printing dictionary")
geek = {"404": "clueless\n", "GOOGLING":"searching the internet for a person\n",
        "UNINSTALLED":"being fired\n"}

f = open("dict1.dat", "wb")

pickle.dump(geek, f)
f.close()

            

