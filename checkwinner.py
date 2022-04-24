#code currently generates a deck, and draws cards from it, can add players. poker hand drawn out.
#hands and table cards are 'mashed' into one list

#value system
#  0,0000000000, first digit declares what type of result, next 10 digits describe the hand



 

from time import perf_counter
from collections import Counter
from jamiepoker import poker as Poker

times = perf_counter()
iterative = 0
while iterative < 1:
    deck = Poker.Deck()
    deck.shuffle()


    player1 = Poker.Player("Jamie")
    player1.drawPokerHand(deck)
    print(player1.name)
    player1.showHand()

    player2 = Poker.Player("Computer")
    player2.drawPokerHand(deck)
    print(player2.name)
    player2.showHand()

    table1 = Poker.CommunityCards()
    print("Table Cards")
    table1.fulltablewithshow(deck)

    
    Poker.CheckWinnerAndPrint(player1,player2,table1)
    iterative += 1

timee = perf_counter()
elapsed = timee - times
print("time = " + str(elapsed))




