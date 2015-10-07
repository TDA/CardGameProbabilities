__author__ = 'saipc'
from Deck import Deck
# This pgm calculates the probability
# of getting a blackjack, with no prior
# info, and no memory

class BlackJack(Deck):
    def calc(self, card):
        return

if __name__ == '__main__':
    # no jokers in bj, so this is fine
    deck = Deck()
    # prob of getting an Ace AND one of Jack or Queen or King or Ten
    P = deck.calcProbabOfCardInAllSuits("Ace") * (
                                    deck.calcProbabOfCardInAllSuits(10) +
                                    deck.calcProbabOfCardInAllSuits("Jack") +
                                    deck.calcProbabOfCardInAllSuits("Queen") +
                                    deck.calcProbabOfCardInAllSuits("King")
                                    )
    print P
    # Lets do one deck, easier to count,
    # and can replicate
    # We might need a separate card
    # counter class :)