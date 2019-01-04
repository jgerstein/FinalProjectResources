# can modify value of a specific ace based on the rest of the hand

class Card:

    def __init__(self, suit, name):
        self.suit = suit
        self.name = name
        self.value = self.get_value(name)
    
    def get_value(self, name):
        values = {'ace': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 11, 'queen': 12, 'king': 13}
        return values[name]

    def __str__(self):
        return f"{self.name} of {self.suit}"
    
    __repr__ = __str__

deck = []

for suit in ['spades', 'diamonds', 'hearts', 'clubs']:
    for name in ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']:
        print(f"{name} of {suit}")
        deck.append(Card(suit, name))

print(deck)
for card in deck:
    print(card.name, card.value)