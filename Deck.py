import Card

class Deck:
    def __init__(self):
        self.contents = []
        self.contents = [ Card(rank, suit) 
                            for rank in Card.RANKS 
                            for suit in Card.SUITS]