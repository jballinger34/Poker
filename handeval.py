
'''
BUGZ:

'''
'''
IDEARZ:

Ranges can be applied by making a list of all hands in the range, randomly picking a hand from that list, and evaluating based off of that, will probably need a much larger
sample size though.

'''


from time import perf_counter
#from collections import Counter
from jamiepoker import poker as Poker

times = perf_counter()
a = []
start = [0,0,0,0]
#z1 = []
#z2 = []
iterative = 0
player1 = Poker.Player("Jamie")
player2 = Poker.Player("Computer")
while iterative < 100000:
    deck = Poker.Deck()
    deck.shuffle()
    table1 = Poker.CommunityCards()
    '''
    ANY SPECIFIC CARDS MUST BE DRAWN FIRST, "" or Random must be drawn after
    CARDS WITH BOTH SUIT AND VALUE WILL BE FORCE MADE SO CANT BE MADE AFTER RANDOM, BECAUSE THEY MIGHT TAKE UP THE SAME SUIT AND VALUE.
    '''
    '''INPUTS: SUITS:["Spades","Clubs","Diamonds","Hearts",""] VALUES[14,2,3,4,5,6,7,8,9,10,11,12,13,""]'''
    player1.DrawSpecificCard(deck,"", 12)
    player1.DrawSpecificCard(deck,"", 12)
    player2.DrawSpecificCard(deck,"Hearts", 7)
    player2.DrawSpecificCard(deck,"Hearts", 6)

    #player1.drawPokerHand(deck)#DRAWS TWO RANDOM
    #player1.DrawOneRandom(deck) # DRAWS ONE RANDOM
    
    table1.fulltable(deck)

    a = Poker.CheckWinner(player1,player2,table1)
    '''
    if a[2] == 1: #WHEN THERE IS A SPLITPOT
        print("p1")
        player1.showHand()
        print("p2")
        player2.showHand()
        print("tablecards")
        for card in table1.communitycards:
            card.show()
        print("left in deck")
        for c in deck.cards:
            c.show()
    '''
    start[0] += a[0]
    start[1] += a[1]
    start[2] += a[2]
    start[3] += a[3]

    '''#counts hand outcomes
    x = Poker.Eval(player1, table1)
    y = Poker.Eval(player2, table1)
    z1.append(x[1])
    z2.append(y[1])
    '''
    #only needed if players are created before loop
    player1.discardHand()
    player2.discardHand()
    iterative += 1
p1winpercent = 100*start[0]/start[3]
p2winpercent = 100*start[1]/start[3]
splitpotpercent = 100*start[2]/start[3]
'''
count1 = Counter(z1)
count2 = Counter(z2)
'''
print(p1winpercent)
#print(count1)
print(p2winpercent)
#print(count2)
print("SplitPot "+ str(splitpotpercent))

timee = perf_counter()
elapsed = timee - times
print("time = " + str(elapsed))





