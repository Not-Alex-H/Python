# Texas Hold'em Poker odds counter
import random
import time
cards = []
_card = ""
def setup_deck():
    while len(cards) < 52:
        value = random.randint(2, 14)
        suit = random.randint(1, 4)
        if suit == 1:
            suit = "♦"
        else:
            if suit == 2:
                suit = "♥"
            else:
                if suit == 3:
                    suit = "♠"
                else:
                    suit = "♣"
        value = random.randint(2, 14)
        if value == 11:
            value = "J"
        if value == 12:
            value = "Q"
        if value == 13:
            value = "K"
        if value == 14:
            value = "A"
        card = str(value) + str(suit)
        if not cards.count(card) > 0:
            cards.append(card)

        
setup_deck()
print(cards)
print(len(cards))