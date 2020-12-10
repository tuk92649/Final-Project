import random

class Card(object):
    suits=("C", "D", "H", "S")
    ranks=(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    def __init__(self, rank, suit):
        self.rank=rank
        self.suit=suit

    #compares the values of two operands and returns True or False
    #based on whether the condition is met.
            
    #equality operator (equal to)
    def __eq__(self, other):
        rank_self=self.rank
        rank_other=other.rank   
        return (rank_self==rank_other)

    #equality operator (not equal to)
    def __ne__(self, other):
        rank_self=self.rank
        rank_other=other.rank 
        return (rank_self!=rank_other)

    #equality operator (less than)
    def __lt__(self, other):
        rank_self=self.rank
        rank_other=other.rank
        return (rank_self<rank_other)

    #equality operator (less than equal to)
    def __le__ (self, other):
        rank_self=self.rank
        rank_other=other.rank 
        return (rank_self<=rank_other)

    #equality operator (greater than)
    def __gt__ (self, other):
        rank_self=self.rank
        rank_other=other.rank
        return (rank_self>rank_other)

    #equality operator (greater than equal to)
    def __ge__ (self, other):
        rank_self=self.rank
        rank_other=other.rank
        return (rank_self>=rank_other)

    def __str__(self):
        rank=str(self.rank)
        return rank + self.suit

class StandardDeck(object):
    def __init__(self):
        self.deck=[]
        #these are for loops, so everytime it chooses a card it appends itself to self.deck
        for suit in Card.suits:
            #referring back to class Card using the values in suits
            for rank in Card.ranks:
                #referring back to class Card using the valus in ranks
                self.deck.append(Card(rank,suit))
              
    #shuffle the deck 1 time
    def shuffle(self, times=1):
        random.shuffle(self.deck)
        print("\n")
        print("Deck Shuffled")
        print("\n")

    def deal(self):
        #pop() removes and returns last value from the list
        return self.deck.pop(0)

class Poker(object):
    def __init__(self, Players):
        self.deck=StandardDeck()
        self.deck.shuffle()
        self.hands=[]
        self.total_point_list=[]       

        for x in range(Players):
            hand=[]
            #5 is the amount of cards in the hand
            for n in range(5):
                deal=self.deck.deal()
                hand.append(deal)
            self.hands.append(hand)

    #point() to calculate score
    def point(self, hand):
        #returns a sorted list
        s_hand=sorted(hand,reverse=True)
        r_list=[]
        #for loop to add the card that was pulled into individual hand
        for card in s_hand:
            r_card=card.rank
            r_list.append(r_card)
        #calculates by taking the cards that have been appended to r_list
        #goes in order of the list
        #multiplies by 13
        #puts it to the power of 5-the position it is in the list
        card_sum=0
        card_sum=r_list[0]*13**4+r_list[1]*13**3+r_list[2]*13**2+r_list[3]*13+r_list[4]
        return card_sum
            
    #High Card is the worst possible hand on the poker hand rankings list.
    #It consists of no pair or any other hand type – just a high card. The words “High Card” should
    #have you thinking straight away about a hand with the highest card.
    def HighCard(self, hand):    
        s_hand=sorted(hand,reverse=True)
        c_hand=True
        hand_value=1
        t_point=hand_value*13**5+self.point(s_hand)
        r_list=[]               
        for card in s_hand:
            card=card.rank
            r_list.append(card)
        if c_hand:
            #append the value calculated for t_point into total_point list
            self.total_point_list.append(t_point)
        else:
            c_hand=False
            #if it is not a High Card pass it on to check if it is a One Pair
            self.OnePair(s_hand)
            
    #One pair, or simply a pair, is a hand that contains two cards of one rank and three cards of three other ranks
    #(the kickers), such as 4♥ 4♠ K♠ 10♦ 5♠ ("one pair, fours" or a "pair of fours"). It ranks below two pair and above high card.
    def OnePair(self, hand):
        s_hand=sorted(hand,reverse=True)
        c_hand=True
        hand_value=2
        t_point=hand_value*13**5+self.point(s_hand)
        r_list=[]                                       
        r_count=[]                                      
        for card in s_hand:
            card=card.rank
            r_list.append(card)
        if c_hand:
            #append the value calculated for t_point into total_point list
            self.total_point_list.append(t_point)  
        else:
            c_hand=False
            #if it is not a One Pair pass it on to check if it is a Two Pair
            self.TwoPair(s_hand)
            
    #Two pair is a hand that contains two cards of one rank, two cards of another rank
    #and one card of a third rank (the kicker), such as J♥ J♣ 4♣ 4♠ 9♥ ("two pair, jacks and fours"
    #or "two pair, jacks over fours" or "jacks up"). It ranks below three of a kind and above one pair.
    def TwoPair(self, hand):
        s_hand=sorted(hand,reverse=True)
        c_hand=True
        hand_value=3
        t_point=hand_value*13**5+self.point(s_hand)
        #need to look at second and fourth value in the list, need to be identical ranking
        r_list=[]
        for card in s_hand:
            card=card.rank
            r_list.append(card)
            if (s_hand[0].rank==s_hand[1].rank) and (s_hand[2].rank==s_hand[3].rank):
                c_hand=True
                #append the value calculated for t_point into total_point list
                self.total_point_list.append(t_point)
            elif (s_hand[0].rank==s_hand[1].rank) and (s_hand[3].rank==s_hand[4].rank):
                _hand=True
                #append the value calculated for t_point into total_point list
                self.total_point_list.append(t_point)
            elif (s_hand[1].rank==s_hand[2].rank) and (s_hand[3].rank==s_hand[4].rank):
                _hand=True
                #append the value calculated for t_point into total_point list
                self.total_point_list.append(t_point)
            else:
                c_hand=False
                #if it is not a Two Pair pass it on to check if it is Three of a Kind
                self.ThreeofaKind(s_hand)

    #Three of a kind, also known as trips or a set, is a hand that contains three cards of
    #one rank and two cards of two other ranks (the kickers), such as 2♦ 2♠ 2♣ K♠ 6♥
    #("three of a kind, twos" or "trip twos" or a "set of twos"). It ranks below a straight and above two pair.
    def ThreeofaKind(self, hand):
        s_hand=sorted(hand,reverse=True)
        c_hand=True
        hand_value=4
        t_point=hand_value*13**5+self.point(s_hand)
        #need to look at the third value in the list, the means location 2
        r_list=[]
        for card in s_hand:
            card=card.rank
            r_list.append(card)
            if (s_hand[0].rank==s_hand[1].rank==s_hand[2].rank):
                c_hand=True
                #append the value calculated for t_point into total_point list
                self.total_point_list.append(t_point)
            elif (s_hand[1].rank==s_hand[2].rank==s_hand[3].rank):
                c_hand=True
                #append the value calculated for t_point into total_point list
                self.total_point_list.append(t_point)
            elif (s_hand[2].rank==s_hand[3].rank==s_hand[4].rank):
                c_hand=True
                #append the value calculated for t_point into total_point list
                self.total_point_list.append(t_point)
            else:
                c_hand=False
                #if it is not Three of a Kind pass it on to check if it is a Straight
                self.Straight(s_hand)

    #A straight is a hand that contains five cards of sequential rank,
    #not all of the same suit, such as 7♣ 6♠ 5♠ 4♥ 3♥ (a "seven-high straight"). It ranks below a flush and above three of a kind.            
    def Straight(self, hand):
        s_hand=sorted(hand,reverse=True)
        c_hand=True
        hand_value=5
        t_point=hand_value*13**5+self.point(s_hand)
        for card in s_hand:
            if card.rank != s_hand[0].rank:
                c_hand=False
            else:
                s_hand[0].rank=s_hand[0].rank-1
        if c_hand:
            #append the value calculated for t_point into total_point list
            self.total_point_list.append(t_point)   
        else:
            c_hand=False
            #if it is not a Straight pass it on to check if it is a Flush
            self.Flush(s_hand)

    #A flush is a hand that contains five cards all of the same suit, not all of sequential rank,
    #such as K♣ 10♣ 7♣ 6♣ 4♣ (a "king-high flush" or a "king-ten-high flush"). It ranks below a full
    #house and above a straight. Under ace-to-five low rules, flushes are not possible (so J♥ 8♥ 4♥ 3♥ 2♥ is a jack-high hand).
    def Flush(self, hand):
        s_hand=sorted(hand,reverse=True)
        c_hand=True
        hand_value=6
        t_point=hand_value*13**5+self.point(s_hand)
        for card in s_hand:
            if c_hand:
                #append the value calculated for t_point into total_point list
                self.total_point_list.append(t_point)
            if not(card.suit==s_hand[0].suit):
                c_hand=False
            else:
                c_hand=False
                #if it is not a Flush pass it on to check if it is a Full House
                self.FullHouse(s_hand)

    #A full house, also known as a full boat or a boat (and originally called a full hand),
    #is a hand that contains three cards of one rank and two cards of another rank, such as 3♣ 3♠ 3♦ 6♣ 6♥
    #(a "full house, threes over sixes" or "threes full of sixes" or "threes full"). It ranks below four of a kind and above a flush.
    def FullHouse(self, hand):  
        s_hand=sorted(hand,reverse=True)
        c_hand=True
        hand_value=7
        t_point=hand_value*13**5+self.point(s_hand)
        r_list=[]
        for card in s_hand:
            card=card.rank
            r_list.append(card)
        if (s_hand[0].rank==s_hand[1].rank==s_hand[2].rank) and (s_hand[3].rank==s_hand[4].rank):
            c_hand=True
            #append the value calculated for t_point into total_point list
            self.total_pointlist.append(t_point)   
        else:
            c_hand=False
            #if it is not a Full House pass it on to check if it is Four of a Kind
            self.FourofaKind(s_hand)

    #Four of a kind, also known as quads, is a hand that contains four cards of one rank and one card of another rank
    #(the kicker), such as 9♣ 9♠ 9♦ 9♥ J♥ ("four of a kind, nines"). It ranks below a straight flush and above a full house.
    def FourofaKind(self, hand):
        s_hand=sorted(hand,reverse=True)
        c_hand=True
        hand_value=8
        #4 identical ranks meaning 2nd ranking must be identitcal rank
        t_point=hand_value*13**5+self.point(s_hand)
        for card in s_hand:
            c=0
            if (s_hand[0].rank==s_hand[1].rank==s_hand[2].rank==s_hand[3].rank):
                c=c+1
        if c_hand:
            hand_value=True
            #append the value calculated for t_point into total_point list
            self.total_point_list.append(t_point)
        else:
            c_hand=False
            #if it is not Four of a Kind pass it on to check if it is a Straight Flush
            self.StraightFlush(s_hand)

    #A straight flush is a hand that contains five cards of sequential rank, all of the same suit,
    #such as Q♥ J♥ 10♥ 9♥ 8♥ (a "queen-high straight flush"). It ranks below five of a kind and above four of a kind.        
    def StraightFlush(self, hand):
        s_hand=sorted(hand,reverse=True)
        c_hand=True
        hand_value=9
        t_point=hand_value*13**5+self.point(s_hand)
        for card in s_hand:
            c=0
            if (s_hand[0].suit==s_hand[1].suit==s_hand[2].suit==s_hand[3].suit==s_hand[4].suit):
                c=c+1
        if c_hand:
            #append the value calculated for t_point into total_point list
            self.total_point_list.append(t_point)
        else:
            c_hand=False
            #if it is not a Straight Flush pass it on to check if it is Four of a Kind
            self.RoyalFlush(s_hand)

    #An ace-high straight flush, such as A♦ K♦ Q♦ J♦ 10♦, is called a royal flush
    #or royal straight flush and is the best possible hand in high games when not using wild cards.
    def RoyalFlush(self, hand):
        s_hand=sorted(hand,reverse=True)
        c_hand=True
        hand_value=10
        t_point=hand_value*13**5+self.point(s_hand)
        for card in s_hand:
            if ((s_hand[0].suit==s_hand[1].suit==s_hand[2].suit==s_hand[3].suit==s_hand[4].suit) or (card.rank != 14)):
                hand_value=False
            else:
                c_rank=14-1
            #append the value calculated for t_point into total_point list
            self.total_point_list.append(t_point)               
            
            
    def play(self):
        length_hands=len(self.hands)
        for n in range(length_hands):
            s_hand=sorted(self.hands[n], reverse=True)
            hand=""
            for card in s_hand:
                hand=hand+str(card)+" "
            print("Player "+str(n + 1)+ ": "+hand)
        
    
def play_game():
    n_hands=int(input("Enter number of players to play: "))
    #to play the game need more than two hands and less than seven
    #if less than 2 or more than seven in inputted statement is reprinted
    while (n_hands<2 or n_hands>7):
        n_hands=int(input("Enter number of players to play: "))
    play_game=Poker(n_hands)
    play_game.play()

    winner=play_game.total_point_list

    for n in range(n_hands):
        play_game.HighCard(play_game.hands[n])

    print("\n")
    m=play_game.total_point_list.index(max(winner))
    print("Player "+str(m+1)+" wins!")
    
play_game()
