#code currently generates a deck, and draws cards from it, can add players. poker hand drawn out.



from time import perf_counter
from collections import Counter
import poker as Poker

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




