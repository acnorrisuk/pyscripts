import random
import pickle

f = open("picklecritter.dat", "wb")

hunger = random.randint(2, 3)
boredom = random.randint(1, 2)
unloved = random.randint(1, 2)
thirsty = random.randint(2, 3)


pickle.dump(hunger)
pickle.dump(boredom)
pickle.dump(unloved)
pickle.dump(thirsty)
f.close()
