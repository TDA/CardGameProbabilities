__author__ = 'saipc'

class Deck:
    def __init__(self,
                 suits = ("Hearts", "Clubs", "Diamonds", "Spades"),
                 normalCards = [x for x in xrange(2, 11, 1)],
                 highCards = ("Ace", "King", "Queen", "Jack"),
                 totalCards = 52):
        self.suits = list(suits)
        # self.normalCards = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
        self.normalCards = normalCards
        self.highCards = list(highCards)
        self.totalCards = totalCards

    def calcProbabOfCard (self, cardName):
        try:
            card, suit = cardName.split(" ")
            suit = suit.lower()
            tempCard = card
            if (suit in (suit.lower() for suit in self.suits)):
                # see if the card is a number or a face card,
                # and continue searching for it appropriately
                try:
                    card = int(card)
                except:
                    card = tempCard.lower()
                # was card a number?
                if isinstance(card, int) and card in self.normalCards:
                    return 1.0 / self.totalCards
                # was card a face card?
                elif (card  in (card.lower() for card in self.highCards)):
                        return 1.0 / self.totalCards
            else:
                return -1
        except:
            print "Enter a valid card"

    def displayDeck(self):
        for suit in self.suits:
            print '{'
            print suit + ' : '
            print ','.join([str(card) for card in self.normalCards + self.highCards])
            print '}'


if __name__ == '__main__':
    deck = Deck()
    x = deck.calcProbabOfCard("8 hearts")
    y = deck.calcProbabOfCard("7 spades")
    # print x , y

    # customize the deck
    halfdeck = Deck(("sai", "pc"),
                    [x for x in xrange(2, 10, 1)],
                    ("Ace", "King", "Queen", "Jack"),
                    24
                    )
    x = halfdeck.calcProbabOfCard("Ace sai")
    #print x

    spanishDeck = Deck(("Hearts", "Clubs", "Diamonds", "Spades"),
                    [x for x in xrange(2, 10, 1)],
                    ("Ace", "King", "Queen", "Jack"),
                    48
                    )
    x = spanishDeck.calcProbabOfCard("Ace Clubs")
    print x
    spanishDeck.displayDeck()
