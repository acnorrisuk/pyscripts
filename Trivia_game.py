# reading plain text files

import sys

def open_file(file_name, mode):
    """open a file"""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open file", file_name, "Ending program\n", e)
        input("press enter to exit")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return formatted next line"""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """returns next block of questions"""
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    return category, question, answers, correct, explanation

def welcome():
    """welcome title"""
    print("\t     WELCOME TO THE TRIVIA CHALLENGE!\n")
    

    
def main():
    trivia_file = open_file("trivia.txt", "r")
    welcome()
    score = 0

    

# get first block

    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print("\t", i+1, "-", answers[i])

#get answer

        answer = input("What's your answer?: ")
    
        if answer == correct:
            print("\nCorrect!\n", end="")
            score += 1
            print(explanation)
            print("Score: ", score, "\n\n")
            input("Press enter for the next question")
        else:
            print("\nIncorrect\n", end="")
            print(explanation)
            print("Score: ", score, "\n\n")
            input("Press enter for the next question: ")

# next block needed

        category, question, answers, correct, explanation = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question")
    print("Your score is: ", score)

main()

input("I hope you have enjoyed playing.\n"
      "Press enter to exit")

    




