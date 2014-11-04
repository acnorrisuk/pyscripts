months_list = ["january","february","march","april","may","june",
               "july","august","september","october","november","december"]


print("I will try to guess your birth month. Please answer 'y' or 'n' to each question")


def answers_yes(letter):
    """removes words without that letter"""
    for month in months_list[:]:
        if letter not in month:
            months_list.remove(month)
      

def answers_no(letter):
    """removes words with that letter"""
    for month in months_list[:]:
        if letter in month:
            months_list.remove(month)
    

def question(letter):
    """asks the question and runs appropriate function"""
    response = None
    while response not in ("y", "n"):
        response = input("\nDoes the month have the letter "+letter+" in it? ")
        response = response.lower()
        if response == 'y':
            answers_yes(letter)
        elif response == 'n':
            answers_no(letter)
        else:
            print("please pick 'y' or 'n'")       


#testing different letters to rule out months
question('a')
if len(months_list) >1:
    for month in months_list:
        if 'a' in month in months_list:
            question('y')
            if 'y' in month in months_list:
                question('r')
                if 'r' in month in months_list:
                    question('b')
                else:
                    question('j')
            else:
                question('r')
                if 'r' in month in months_list:
                    question('h')
                else:
                    question('l')
        else:
            question('m')
            for month in months_list:
                if 'm' in month in months_list:
                    question('n')
                    if 'n' in month in months_list:
                        question('s')
                    else:
                        question('p')
                else:
                    question('j')
                    if 'j' in month in months_list:
                        question('l')
                    else:
                        question('r')


print("\nIt's",months_list)

input("\n\nPress any key to exit ")



