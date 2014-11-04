# function parameters and return values

def display(message):
    print(message)

def give_me_five():
    five = 5
    return five

def ask(question):
    """ Yes/no question """
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

display("here's a message\n")

number = give_me_five()
print("Here is give_me_5():", number)

answer = ask("\nenter 'y' or 'n': ")
print("Thanks for entering", answer)

input("exit")
