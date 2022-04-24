from time import perf_counter
from collections import Counter
from jamiepoker import poker as Poker


times = perf_counter()
iterative = 0
a = []
while iterative < 100000:
    deck = Poker.Deck()
    deck.shuffle()
    
    player1 = Poker.Player("Jamie")
    player1.drawPokerHand(deck)

    player2 = Poker.Player("Computer")
    player2.drawPokerHand(deck)

    table1 = Poker.CommunityCards()
    table1.fulltable(deck)

    
    b = (Poker.Eval(player1,table1))
    a.append(b[1])
    
    iterative += 1
count = Counter(a)
print(count)

timee = perf_counter()
elapsed = timee - times
print("time = " + str(elapsed))

