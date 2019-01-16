import random

cards = {
    'heart': {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5
    },
    'diamond': {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5
    }
}

def get_card(deck):
    print(deck)
    suit = random.choice(list(cards.keys()))
    print(suit)
    card = random.choice(list(cards[suit].keys()))
    print(card)
    del cards[suit][card]
    return card

new_card = get_card(cards)