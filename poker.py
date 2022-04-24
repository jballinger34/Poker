import random
from collections import Counter


class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    
    def show(self):
        print("{} of {}".format(self.value, self.suit))
        
class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for s in ["Spades","Clubs","Diamonds","Hearts"]:
            for v in range(2,15): #was 1-14, but 2-15 may be appropriate, 2 low, 15 ace high
                self.cards.append(Card(s,v))
                #print("{} of {}".format(v,s))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

    def ChooseSpecificCard(self,s,v):
        if s == "" and v == "":
            return self.drawCard()
        if s == "":
            val = int(v)
            vallist = []
            for b in self.cards:
                if b.value == val:
                    vallist.append(b)
            card1 = random.choice(vallist)
            self.cards.remove(card1)
            return card1
        if v == "":
            suitlist = []
            for c in self.cards:
                if c.suit == s:
                    suitlist.append(c)
            card2 = random.choice(suitlist)
            self.cards.remove(card2)
            return card2
        for a in self.cards:
            if a.suit == s and a.value == v:
                    self.cards.remove(a)
                    return a
                         
class CommunityCards(object):
    def __init__(self):
        self.communitycards = []

    def Flop(self,deck):
        self.communitycards.append(deck.drawCard())
        self.communitycards.append(deck.drawCard())
        self.communitycards.append(deck.drawCard())
        for card in self.communitycards:
            card.show()
    
    def Turn(self,deck):
        self.communitycards.append(deck.drawCard())
        for card in self.communitycards:
            card.show()

    def River(self,deck):
        self.communitycards.append(deck.drawCard())
        for card in self.communitycards:
            card.show()
    
    def fulltable(self,deck):
        self.communitycards.append(deck.drawCard())
        self.communitycards.append(deck.drawCard())
        self.communitycards.append(deck.drawCard())
        self.communitycards.append(deck.drawCard())
        self.communitycards.append(deck.drawCard())

    def fulltablewithshow(self,deck):
        self.communitycards.append(deck.drawCard())
        self.communitycards.append(deck.drawCard())
        self.communitycards.append(deck.drawCard())
        self.communitycards.append(deck.drawCard())
        self.communitycards.append(deck.drawCard())
        #shows table with fulltable call
        for card in self.communitycards:
            card.show()
    

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def drawPokerHand(self, deck):
        self.hand.append(deck.drawCard())
        self.hand.append(deck.drawCard())
    
    def showHand(self):
        for card in self.hand:
            card.show()

    def discardHand(self):
        self.hand.clear()
        self.eval = 0

    def DrawOneRandom(self,deck):
        self.hand.append(deck.drawCard())
    
    def DrawSpecificCard(self,deck,s,v):
        self.hand.append(deck.ChooseSpecificCard(s,v))
    

        
def Eval(player,table): #probably a better way to do this
    mash = Card7hand(player,table)
    score = 0
    result = ""
    sf = CheckSF(mash)
    if sf[0]:
        score += 80000000000
        score += sf[1]
        result = "Straight Flush"

    if score == 0:
        q = CheckQuads(mash)
        if q[0]:
            score += 70000000000
            score += q[1]
            result = "Quads"

    if score == 0:
        fh = CheckFH(mash)
        if fh[0]:
            score += 60000000000
            score += fh[1]
            result = "Full House"

    if score == 0:
        f = CheckF(mash)
        if f[0] :
            score += 50000000000
            score += f[1]
            result = "Flush"

    if score == 0:
        s = CheckS(mash)
        if s[0]:
            score += 40000000000
            score += s[1]
            result = "Straight"

    if score == 0:
        t = CheckTrips(mash)
        if t[0]:
            score += 30000000000
            score += t[1]
            result = "Trips"

    if score == 0:
        tp = CheckTP(mash)
        if tp[0]:
            score += 20000000000
            score += tp[1]
            result = "Two Pair"

    if score == 0:
        p = CheckPair(mash, False)
        if p[0]:
            score += 10000000000
            score += p[1]
            result = "Pair"

    if score == 0:
        hc = CheckHC(mash)
        score += hc
        result = "High Card"
    
    return score, result

def CheckWinner(player1, player2, table):
    p1s = Eval(player1, table)
    score1 = p1s[0]
    p2s = Eval(player2, table)
    score2 = p2s[0]
    if score1 > score2:
        return [1,0,0,1]
    elif score2 > score1:
        return [0,1,0,1]
    else:
        return [0,0,1,1]

#needs work to be used for hand eval
def CheckWinnerMultiWay(players,table):
    if len(players) > 1:
        for player in players:
            a = Eval(player,table)
            player.eval = a[0]
    evals = []
    for player in players:
        evals.append(player.eval)
    w = max(evals)
    winners = []
    for player in players:
        if player.eval == w:
            winners.append(player)

def CheckWinnerAndPrint(player1, player2, table):
    p1s = Eval(player1, table)
    score1 = p1s[0]
    result1 = p1s[1]
    p2s = Eval(player2, table)
    score2 = p2s[0]
    result2 = p2s[1]
    if score1 > score2:
        print(player1.name+ " Wins With: " + result1 + ", Against: " + result2)
        return [1,0,0,1]
    elif score2 > score1:
        print(player2.name+ " Wins With: " + result2 + ", Against: " + result1)
        return [0,1,0,1]
    else:
        print("splitpot")
        return [0,0,1,1]

def Card7hand(player,table):
    playerandtable = []
    for c in player.hand:
        playerandtable.append(c)
    for c in table.communitycards:
        playerandtable.append(c)

    return playerandtable

def CheckS(tobechecked):
    #checks straight given any number of cards
    values = []
    for c in tobechecked:
        values.append(c.value)
    #print(values)
    values.sort()
    #MAX VALUE GIVES THE HIGH CARD IN THE STRAIGHT
    #print(values)
    hc = int
    straight = False
    values = list(dict.fromkeys(values)) # REMOVES DUPLICATES # IMPORTANT LINE
    #print(values)
    for i in range(len(values),0,-1): #looping through 7,6,5,4,3,2,1 or 5,4,3,2,1
        if values[i-1] == values[i - 2]+1 and values[i - 2] == values[i - 3]+1 and values[i - 3] == values[i - 4]+1 and values[i-4] == values[i-5]+1:
            straight = True
            hc = (values[i-1])
            return straight, hc
    if values[len(values)-1] == 14 and values[0] == 2 and values[1] == 3 and values[2] == 4 and values[3] == 5:
        hc = values[3]
        straight = True
        return straight, hc
    return straight, hc
    
def CheckF(tobechecked):
    suits = []
    flush = False
    highcards = int
    for cards in tobechecked:
        suits.append(cards.suit)
    #print(suits) # prints the cards suits
    count = Counter(suits)
    d,s,c,h = count['Diamonds'],count['Spades'],count['Clubs'],count['Hearts']
    if d >= 5:
        flush = True
        flushlist = tobechecked
        for card in flushlist:
            if card.suit != 'Diamonds':
                flushlist.remove(card)
        highcards = CheckHC(flushlist)
        return flush, highcards, flushlist
    if s >= 5:
        flush = True
        flushlist = tobechecked
        for card in flushlist:
            if card.suit != 'Spades':
                flushlist.remove(card)
        highcards = CheckHC(flushlist)
        return flush, highcards, flushlist
    if c >= 5:
        flush = True
        flushlist = tobechecked
        for card in flushlist:
            if card.suit != 'Clubs':
                flushlist.remove(card)
        highcards = CheckHC(flushlist)
        return flush, highcards, flushlist
    if h >= 5:
        flush = True
        flushlist = tobechecked
        for card in flushlist:
            if card.suit != 'Hearts':
                flushlist.remove(card)
        highcards = CheckHC(flushlist)
        return flush, highcards, flushlist
    return flush, highcards

def CheckSF(tobechecked):
    sf = False
    high = int
    a = CheckF(tobechecked)
    if a[0]:
        flushlist = a[2]
        b = CheckS(flushlist)
        if b[0]:
            sf = True
            high = b[1]
        return sf, high
    return sf, high
        
def CheckQuads(tobechecked):
    values = []
    for c in tobechecked:
        values.append(c.value)
    values.sort()
    hc = ""
    kicker = int
    qv = str
    quadvalue = int
    quads = False
    for i in range(len(values),0,-1):
        if values[i-1] == values[i - 2] and values[i - 2] == values[i - 3] and values[i - 3] == values[i - 4]:  #4 of the same value!
            hc = (values[i-1])
            values.remove(hc)
            values.remove(hc)
            values.remove(hc)
            values.remove(hc)
            kicker = max(values)
            qv = str(hc) + str(kicker)
            quadvalue = int(qv)
            #print(str(hc) +" QUADS, with " +str(kicker)+" kicker")
            quads = True
            break
    return quads, quadvalue
    
def CheckFH(tobechecked):
    returned = CheckTrips(tobechecked)
    values = []
    fullhouse = False
    pairkicker = int
    for c in tobechecked:
        values.append(c.value)
    if returned[0]:
        triphc = returned[2]
        values.remove(triphc)
        values.remove(triphc)
        values.remove(triphc) #values now includes the 4 cards that are not the trips
        values.sort()
        pair = CheckPair(values, True)
        if pair[0]: #pair is present with trips .... fullhouse!
            pairkicker = pair[2]
            #print("FH, set of "+ str(triphc)+ "'s with " +str(pairkicker)+ " pair")
            fullhouse = True
            return fullhouse, pairkicker
    return fullhouse, pairkicker
    
def CheckTrips(tobechecked):
    values = []
    for c in tobechecked:
        values.append(c.value)
    values.sort()
    triphc = int
    tv = str
    k1 = int
    k2 = int
    tripvalue = int
    trips = False
    #print("s" + str(values))
    for i in range(len(values),0,-1):
        if values[i-1] == values[i - 2] and values[i - 2] == values[i - 3]:
            triphc = values[i-1]
            values.remove(triphc)
            values.remove(triphc)
            values.remove(triphc)
            a = '%02d' % triphc
            trips = True
            kicker1 = values[len(values)-1]
            kicker2 = values[len(values)-2]
            k1 = '%02d' % kicker1
            k2 = '%02d' % kicker2
            tv = str(a) + str(k1) + str(k2)
            tripvalue = int(tv)
            return trips, tripvalue, triphc   
    return trips, tripvalue, triphc

def CheckTP(tobechecked):
    values = []
    for c in tobechecked:
        values.append(c.value)
    twopair = False
    pair1 = int
    pair2 = int
    tpv = str
    kicker = int
    twopairvalue = int
    values.sort()
    a = CheckPair(values, True)
    if a[0]:
        pair1 = a[2]
        values.remove(pair1)
        values.remove(pair1)
        pair1 = '%02d' % pair1
        b = CheckPair(values, True)
        if b[0]:
            twopair = True
            pair2 = b[2]
            values.remove(pair2)
            values.remove(pair2)
            pair2 = '%02d' % b[2]
            kicker = max(values)
            k = '%02d' % kicker
            tpv = str(pair1) + str(pair2) + str(k)
            twopairvalue = int(tpv)
            #print("tp")
    return twopair, twopairvalue
        
def CheckPair(tobechecked, fromFH):
    values = []
    pairof = int
    pair = False
    pairvalue = int
    formattedpairof = int
    pv = str
    k1 = int
    k2 = int
    k3 = int
    if fromFH:
        for c in tobechecked:
            values.append(c)
    else:
        for c in tobechecked:
            values.append(c.value)
    values.sort()
    for i in range(len(values)-1,0,-1):
            if values[i] == values[i-1] :  #2 of the same value!
                #pair is present
                pair = True
                pairof = (values[i])
                values.remove(pairof)
                values.remove(pairof)
                formattedpairof = '%02d' % pairof
                if fromFH:
                    return pair, pairvalue, pairof
                else:
                    k1 = max(values)
                    values.remove(k1)
                    k1 = '%02d' % k1
                    k2 = max(values)
                    values.remove(k2)
                    k2 = '%02d' % k2
                    k3 = max(values)
                    values.remove(k3)
                    k3 = '%02d' % k3
                    pv = str(formattedpairof) + str(k1) + str(k2) + str(k3)
                    pairvalue =int(pv)
                    return pair, pairvalue, pairof
    return pair, pairvalue, pairof

def CheckHC(tobechecked):
    values = []
    highcards = 0
    for cards in tobechecked:
        values.append(cards.value)
    values.sort()
    l = len(values)-1
    a,b,c,d,e = '%02d' % values[l],'%02d' % values[l-1],'%02d' % values[l-2],'%02d' % values[l-3],'%02d' % values[l-4]
    hc = str(a) + str(b) +str(c) + str(d) + str(e)
    highcards = int(hc)
    #print("hc")
    return highcards

