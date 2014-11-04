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
    print("\n\t     WELCOME TO TRIVIA CHALLENGE!")


def main():
    welcome()
    score = 0
    print(
        """
    1 Science and Technology
    2 Film and TV
    3 Music
    4 General Knowledge
    """
        )

    pick = input("Please choose a category: ")

    if pick == "1":
        trivia_file = open_file("science.txt", "r")

    elif pick == "2":
        trivia_file = open_file("film.txt", "r")

    elif pick == "3":
        trivia_file = open_file("music.txt", "r")

    elif pick == "4":
        trivia_file = open_file("general.txt", "r")

    else:
        print("Please repeat your choice: \n")
        return main()

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
            input("Press enter for the next question")
        else:
            print("\nIncorrect\n", end="")
            print(explanation)
            input("Press enter for the next question: ")

# next block needed

        category, question, answers, correct, explanation = next_block(trivia_file)

    trivia_file.close()

    print("\nThat was the last question in this round")
    print("Your score for this round is: ", score, " out of 5\n")
    

    again = input("\nWould you like to try another category? (y,n): ")

    if again == "n":
        print("I hope you have enjoyed playing")
    else:
        main()

main()

input("\nPress enter to exit")





