
fib = ("0, 1, 1, 2, 3, 5, 8, 13...")
prime = ("2, 3, 5, 7, 9, 11, 13...")
tri = ("3, 6, 10, 15, 21, 28, 36...")

choice = input("welcome to sequences, would you like Fibbonachi, prime or triangular? ")
if choice == "fibbonachi":
    print(fib)    
elif choice == "prime":
    print(prime)
elif choice == "triangular":
    print(tri)
else:
    print("I'm sorry can you repeat your choice")

input("\nexit")
