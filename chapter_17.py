import random

# The exercises require the classes below.

class Card:
    """Represents a standard playing card."""

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        rank_name = Card.rank_names[self.rank]
        suit_name = Card.suit_names[self.suit]
        return f"{rank_name} of {suit_name}"

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        c1 = (self.suit, self.rank)
        c2 = (other.suit, other.rank)
        return c1 < c2

    def __le__(self, other):
        c1 = (self.suit, self.rank)
        c2 = (other.suit, other.rank)
        return c1 <= c2

class Deck:
    """Represents a deck of cards."""

    def __init__(self, cards):
        self.cards = cards

    @staticmethod
    def make_cards():
        cards = []
        for suit in range(4):
            for rank in range(2, 15): # starting with rank 2, ending with rank 14 ("Ace")
                card = Card(suit, rank)
                cards.append(card)
        return cards

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def take_card(self):
        return self.cards.pop()

    def put_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label = ""):
        self.label = label
        self.cards = []

    def move_cards(self, other, num):
        for _ in range(num):
            card = self.take_card()
            other.put_card(card)

class BridgeHand(Hand):
    """Represents a bridge hand."""

    hcp_dict = {
        'Ace': 4,
        'King': 3,
        'Queen': 2,
        'Jack': 1,
    }

    def high_card_point_count(self):
        count = 0
        for card in self.cards:
            rank_name = Card.rank_names[card.rank]
            count += BridgeHand.hcp_dict.get(rank_name, 0)
        return count





# EXERCISE 1
# Ask a chatbot. No code. Not relevant here.
# -----------





# EXERCISE 2
# In the Trick class below, write a method called "find_winner" that loops through the cards in the trick and finds the winner.
# -----------

class Trick(Deck):
    """Represents a trick in contract bridge."""
    
    def find_winner(self):
        led_suit = self.cards[0].suit
        winner_index = 0
        highest_rank = self.cards[0].rank
        
        for i in range(1, len(self.cards)):
            card = self.cards[i]
            if card.suit == led_suit and card.rank > highest_rank:
                highest_rank = card.rank
                winner_index = i
        return winner_index

cards = [Card(1, 3),
        Card(1, 10),
        Card(1, 12),
        Card(2, 13)]

trick = Trick(cards)
print("Cards in trick:")
print(trick)
winner = trick.find_winner()
print(f"Index of winner: {winner}, card: {trick.cards[winner]}")
print()





# EXERCISE 3
# Use and update the PokerHand class with a "has_flush" method.
# Methods from the other exercises will also be added here.
# ------------

class PokerHand(Hand):
    """Represents a poker hand."""
    
    def get_suit_counts(self):
        counter = {}
        for card in self.cards:
            key = card.suit
            counter[key] = counter.get(key, 0) + 1
        return counter
    
    def get_rank_counts(self):
        counter = {}
        for card in self.cards:
            key = card.rank
            counter[key] = counter.get(key, 0) + 1
        return counter
    
    
    
    # added in exercise 3
    def has_flush(self):
        for count in self.get_suit_counts().values():
            if count >= 5:
                return True
        return False
    
    
    
    # added for exercise 4
    def has_straight(self):        
        ranks = list(self.get_rank_counts().keys())
        if 14 in ranks:
            ranks.append(1)
        ranks = sorted(ranks)
        
        streak = 1
        for i in range(1,len(ranks)):
            if ranks[i] == ranks[i-1] + 1:
                streak += 1
                if streak >= 5:
                    return True
            else:
                streak = 1
        
        return False
    
    
    
    # added for exercise 5
    def has_straight_flush(self):
        if not self.has_flush():
            return False
        
        suits = self.get_suit_counts()
        flush_suit = None
        for suit in suits:
            if suits[suit] >= 5:
                flush_suit = suit
                break
                
        flush_hand = PokerHand()
        for card in self.cards:
            if card.suit == flush_suit:
                flush_hand.put_card(card)
        
        return flush_hand.has_straight()
    
    
    
    # added for exercise 6
    def has_pair(self):
        ranks = self.get_rank_counts()
        for value in ranks.values():
            if value >= 2:
                return True
        return False
    
    
    
    # added for exercise 7
    def has_full_house(self):
        has2 = False
        has3 = False
        
        ranks = self.get_rank_counts()
        
        for value in ranks.values():
            if value == 2:
                has2 = True
            elif value == 3:
                has3 = True
        
        return has2 and has3


# setup for exercises 3 - 7
cards = Deck.make_cards()
deck = Deck(cards)
deck.shuffle()
hand = PokerHand()
Hand.move_cards(deck, hand, 7)
print("Cards in hand:")
print(hand)
print()


# testing exercise 3
if hand.has_flush():
    print("We have a flush!")
else:
    print("No flush.")





# EXERCISE 4
# Write a "has_straight" method.
# -----------

# method was added to exercise 3, tested here
if hand.has_straight():
    print("We have a straight!")
else:
    print("No straight.")





# EXERCISE 5
# Write a method for a straight flush.
# -----------

# added to exercise 3, tested here
if hand.has_straight_flush():
    print("We have a straight flush!")
else:
    print("No straight flush.")





# EXERCISE 6
# Write a function to check if a hand has a pair.
# -----------

# added to exercise 3, tested here
if hand.has_pair():
    print("We have a pair!")
else:
    print("No pair.")





# EXERCISE 7
# Write a function to check if the hand has a full house.
# -----------

# added to exercise 3, tested here
if hand.has_full_house():
    print("We have a full house!")
else:
    print("No full house.")





# EXERCISE 8
# Ask a chatbot why the following class is not working properly.

class Kangaroo:
    """A Kangaroo is a marsupial."""
    
    def __init__(self, name, contents=[]):
        """Initialize the pouch contents.

        name: string
        contents: initial pouch contents.
        """
        self.name = name
        self.contents = contents

    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.

        item: object to be added
        """
        self.contents.append(item)

# ---------------------------------

# The chatbot accurately recognizes that because the "contents" parameter is initialized to an empty list,
# when the class and __init__ function objects are created all instances of the Kangaroo class will share the same contents if not provided as an argument.
# To fix this, we should not use a default empty list as the parameter. Instead, we should check in the body of the method if "contents" is None.

def __init__should_look_like_this(self, name, contents = None):
    self.name = name
    
    if contents is None:
        contents = []
        
    self.contents = contents
