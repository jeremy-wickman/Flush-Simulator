#HOW MANY UNTIL I GET A FLUSH?

import random

def get_non_negative_int(prompt):
    while True:
        try:
            value = int(raw_input(prompt))
        except ValueError:
            print("Sorry, that's not a valid response")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value

def deal(i):
    card = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    card_suit = ['c','d','h','s']
    deck=[]
    for i in range(4):
        for j in range(13):
            deck.append(card[j]+card_suit[i])
    random.shuffle(deck) #shuffle the deck
    player1_hand = [] #deal player 1 five cards from the deck
    for x in range(5):
        player1_hand.append(deck.pop(x))
    return player1_hand

simulations = get_non_negative_int("How many simulations would you like to run? ")
flush_count=0

for i in range(simulations):
    player1_hand = deal(i)
    player1_suits = ""
    for j in range(5):
        player1_suits = player1_suits + player1_hand[j][1]
    if player1_suits[0] == player1_suits[1] == player1_suits[2] == player1_suits[3] == player1_suits[4]:
        print "Simulation %s : %s ******You have a flush!*******" %(i, player1_suits)
        flush_count = flush_count + 1
    else:
        pass
        
print "You had %d flushes." %flush_count
print "That's a probability of %0.5f " %(flush_count / float(simulations))
