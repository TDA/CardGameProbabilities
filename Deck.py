__author__ = 'saipc'

class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        # self.normalCards = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
        self.normalCards = [x for x in xrange(2, 11, 1)]
        self.highCards = ["Ace", "King", "Queen", "Jack"]
        self.totalCards = 52

    def calcProbabOfCard (self, cardName):
        try:
            card, suit = cardName.split(" ")
            if (suit in (suit.lower() for suit in self.suits) and
                (int(card) in self.normalCards) or (card  in (card.lower() for card in self.highCards))):
                return 1.0 / self.totalCards
            else:
                return -1
        except:
            print "Enter a valid card"
    def displayDeck(self):
        for suit in self.suits:
            for card in self.normalCards:
                print str(card) + " " + suit
            for card in self.highCards:
                print str(card) + " " + suit

deck = Deck()
x = deck.calcProbabOfCard("8 hearts")
print x
