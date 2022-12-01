#blackjack
import time
import random
import os
import sys

suit = ""
value = ""
card = ""
hand_values_totals = 0
deck = []
hand = []
dealer = []
deck_values = []
hand_values = []
dealer_values = []
hand_no = 0
gamestage = 0
dealer_values_totals = 0
money = 50000
bet = 0
# this is getting all the functions set up
def setup_deck():
    deck.clear()
    while len(deck) < 52:
        suit = random.randint(1, 4)
        match suit:
            case 1:
                suit = "♦"
            case 2:
                suit = "♥"
            case 3:
                suit = "♠"
            case 4:
                suit = "♣"
        value = random.randint(2, 14)
        
        match value:
            case 10:
                value = "T"
            case 11:
                value = "J"
            case 12:
                value = "Q"
            case 13:
                value = "K"
            case 14:
                value = "A"
        card = str(value) + str(suit)
        if not deck.count(card) > 0:
            deck.append(card)
        match value:
            case "T":
                value = 10
            case "J":
                value = 10
            case "Q":
                value = 10
            case "K":
                value = 10
            case "A":
                value = 11
        deck_values.append(value)            
            
def deal():
    for _ in range(2):
        hand.append(deck[0])
        hand_values.append(deck_values[0])
        deck.pop(0)
        deck_values.pop(0)
        dealer.append(deck[0])
        dealer_values.append(deck_values[0])
        deck_values.pop(0)
        deck.pop(0)
    print("Your cards           Dealer's card(s)")
    print("-----------------------------------")
    print("  " + str(hand[0]) + " " + str(hand[1]) + "                  " + str(dealer[0]), end= "\n")
def hit(): 
    global hand_values_totals  
    global action
    global gamestage
    if action == "hit":
            hand.append(deck[0])
            hand_values.append(deck_values[0])
            deck.pop(0)
            deck_values.pop(0)
            os.system('cls')
            print("Your cards           Dealer's card(s)")
            print("-----------------------------------")
            hand_values_totals = 0
            i = 0
            for i in range(int(len(hand))):
                print(" " + hand[i], end = "")
            print("                  " + str(dealer[0]), end = "\n")
            i = 0
            for i in range(0, int(len(hand_values))):
                hand_values_totals = int(hand_values_totals) + int(hand_values[i])
            if hand_values_totals > 21:
                if 11 in hand_values:
                    hand_values.remove(11)
                    hand_values.append(1)
                else:
                    gamestage = "bust"
            action = ""
            time.sleep(0.2)
def stand():
    global gamestage
    global action
    if action == "stand":
        gamestage = "flip"
        action = ""
        time.sleep(0.2)
def double():
    global bet
    if action == "double down":
        bet = int(bet) * 2
        hit()
def split():
    hand.insert("|", 1)
   
       
# Now we begin playing
while True:
    os.system('cls')
    bet = input("You have $" + str(money) + "\n" + "How much do you wanna bet?" + "\n")
    hand.clear()
    hand_values.clear()
    dealer.clear()
    dealer_values.clear()
    gamestage = "deal"
    deck_values.clear()
    os.system('cls')
    setup_deck()
    deal()
    # Starting from here, you can interact with the game
    gamestage = "dealt"
    while gamestage == "dealt":
        action = input()
        if action == "print_data":
            i = 0
            hand_values_totals = 0
            for i in range(0, int(len(hand_values))):
                hand_values_totals = int(hand_values_totals) + int(hand_values[i])
            i = 0
            dealer_values_totals = 0
            for i in range(0, int(len(hand_values))):
                    dealer_values_totals = int(dealer_values_totals) + int(dealer_values[i])
            print("Your total: " + str(hand_values_totals))
            print("Dealer total: " + str(dealer_values_totals))
        hit()
        stand()
        double()
    if gamestage == "bust":
        print("You lose")
        money = int(money) - int(bet)
    if gamestage == "flip":
        dealer_values_totals = 0
        i = 0
        for i in range(0, int(len(dealer_values))):
            dealer_values_totals = int(dealer_values_totals) + int(dealer_values[i])
        while dealer_values_totals < 17:
            dealer.append(deck[0])
            dealer_values.append(deck_values[0])
            deck.pop(0)
            deck_values.pop(0)
            i = 0
            dealer_values_totals = 0
            for i in range(0, int(len(dealer_values))):
                dealer_values_totals = int(dealer_values_totals) + int(dealer_values[i])
            if dealer_values_totals > 21:
                gamestage = "Dealer bust"
        os.system('cls')
        print("Your cards           Dealer's card(s)")
        print("-----------------------------------")
        i = 0
        for i in range(int(len(hand))):
            print(" " + str(hand[i]), end = "")
        print("              ", end = "")
        i = 0
        for i in range(int(len(dealer))):
            print(" " + str(dealer[i]), end = "")
            gamestage = "result"
    if gamestage == "Dealer bust":
        print("You win!")
        money = int(money) + int(bet)
    if gamestage == "result": 
        print("\n")   
        hand_values_totals = 0
        dealer_values_totals = 0
        i = 0
        for i in range(len(hand)):
            hand_values_totals = int(hand_values_totals) + int(hand_values[i])
        i = 0
        for i in range(len(dealer_values)):
            dealer_values_totals = int(dealer_values_totals) + int(dealer_values[i])
        if hand_values_totals > dealer_values_totals:
            print("You win!")
            money = int(money) + int(bet)
        else:
            if hand_values_totals < dealer_values_totals:
                if dealer_values_totals > 21:
                    print("You win!")
                    money = int(money) + int(bet)
                else:        
                    print("You lose")
                    money = int(money) - int(bet)
            else:
                print("tie")
    time.sleep(1)
    # proper splitting has yet to be added