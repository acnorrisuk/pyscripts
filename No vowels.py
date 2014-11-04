# constants and for loops

message = input("Enter a message: ")
new_message = ""
VOWELS = "aeiou"

print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("New string: ", new_message)

print("Your message without vowels is ", new_message)

input("\nexit")
