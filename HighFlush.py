__author__ = 'saipc'
from Deck import Deck


if __name__ == '__main__':
    deck = Deck()
    # deck.displayDeck()
    # we are dealt 7 cards, lets try calculating
    # the probabilities of 1-7 cards being same suit
    for x in xrange(1, 8):
        print deck.calcProbability(x, 52)