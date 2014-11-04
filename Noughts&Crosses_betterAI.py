# constants

X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9



# instructions

def display_instruct():
    """Display game instructions"""
    
    print(
        """
    'Prepare yourself. I am the master of Noughts and Crosses
         Though you may try, you will be no match for me.'

    To make a move you should enter a number: 0 - 8
    The number corresponds to a board position below:


                        0 | 1 | 2
                        ---------
                        3 | 4 | 5
                        ---------
                        6 | 7 | 8

    \n """
        )

# functions

def ask_yes_no(question):
    """Ask a Y/N Question"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Ask for a number 0-8"""
    response = None
    while response not in range(0, 9):
        response = int(input(question))
    return response

def pieces():
    """player or comp first"""
    go_first = ask_yes_no("Would you like to go first? (y/n): ")
    if go_first == "y":
        print("\nYou are 'X' Take the first move")
        human = X
        computer = O
    else:
        print("\nI am 'X'. I will go first")
        computer = X
        human = O
    return computer, human

def new_board():
    """create new board"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """display board"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    """legal moves"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """determine winner"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def human_move(board, human):
    """ human move """
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("\nWhere would you like to go? (0 - 8): ", O, NUM_SQUARES)
        if move not in legal:
            print("That square is already occupied\n")
    print("OK")
    return move

def computer_move(board, computer, human):
    """computer move"""
#making a copy to work with
    board = board[:]

# AI

    
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("I will take square", end=" ")

# winning move

    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
     
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

# next turn

def next_turn(turn):
    """Switch turns"""
    if turn == X:
        return O
    else:
        return X

# congrats

def congrat_winner(the_winner, computer, human):
    """ Congrats to winner """
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie\n")

    if the_winner == computer:
        print("I knew I would beat you all along")

    elif the_winner == human:
        print("I can't believe you beat me!")

    elif the_winner == TIE:
        print("You were very lucky. Next time I will win!")

# main

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

# start

main()

input("\nPress enter to exit")
    

