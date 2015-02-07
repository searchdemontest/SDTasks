#This is a small program that aims to print out a list of cards in a pack of playing cards
#However when printing, it instead prints out the same card 52 time.
#For example,
##>>> 
##King of Spades
##King of Spades
##King of Spades
##King of Spades
##King of Spades
##King of Spades
##King of Spades
##King of Spades
##....

#Please try to debug this so that it prints out the deck list correctly

class Card:
    def __init__(self, suit = 0, rank = 2):
        Card.suit = suit
        Card.rank = rank
#Two class attributes that are helpful in determining suit/rank
    ranklist = ['narf', 'Ace', 'One', 'Two', 'Three', 'Four', 'Five' \
'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    suitlist = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    def __repr__(self):
        return (self.ranklist[self.rank] + " of " + self.suitlist[self.suit])

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit,rank))
                
    def printDeck(self):
        for card in self.cards:
            print(card)
            
    def __repr__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " + str(self.cards[i]) + "\n"
        return s
    
deck = Deck()
deck.printDeck()

