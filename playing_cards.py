# combining objects

class Card(object):
    """ A playing card """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8",
             "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

# hand class

class Hand(object):
    """ A hand of playing cards """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

# main

card1 = Card(rank = "A", suit = "c")
card2 = Card(rank = "2", suit = "c")
card3 = Card(rank = "3", suit = "c")
card4 = Card(rank = "4", suit = "c")
card5 = Card(rank = "5", suit = "c")
card6 = Card(rank = "6", suit = "c")
card7 = Card(rank = "7", suit = "c")
card8 = Card(rank = "8", suit = "c")
card9 = Card(rank = "9", suit = "c")
card10 = Card(rank = "10", suit = "c")
cardJ = Card(rank = "J", suit = "c")
cardQ = Card(rank = "Q", suit = "c")
cardK = Card(rank = "K", suit = "c")

print(card1, card2, card3, card4, card5, card6,
      card7, card8, card9, card10, cardJ, cardQ,
      cardK)

# my hand

my_hand = Hand()
print(my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print(my_hand)

# your hand

your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("Your hand:")
print(your_hand)
print("My hand:")
print(my_hand)

my_hand.clear()
print("clearing hand")
print(my_hand)

input("exit")









