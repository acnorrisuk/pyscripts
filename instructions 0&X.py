# create own functions

def instructions():
    """Display game instructions"""
    
    print(
        """
    Prepare yourself. I am the master of Noughts and Crosses
    Though you may try, you will be no match for me.

    To make a move you should enter a number: 0 - 8
    The number corresponds to a board position below:


                        0 | 1 | 2
                        ---------
                        3 | 4 | 5
                        ---------
                        6 | 7 | 8

    \n """
        )

# Main

instructions()

input("\nexit")
