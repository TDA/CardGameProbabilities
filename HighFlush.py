__author__ = 'saipc'
from Deck import Deck


if __name__ == '__main__':
    deck = Deck()
    # deck.displayDeck()
    # we are dealt 7 cards, lets try calculating
    # the probabilities of 1-7 cards being same suit
    for x in xrange(1, 8):
        # simple probab, assuming replacement,
        # no joker, and 52 card deck, forget this.
        y = x
        P = 1
        # complex probability, a la compound interest
        # no replacement, real life scenario
        while y > 0:
            y = y - 1
            # print 13 - y, 52.0 - y
            P = P * deck.calcProbability(13 - y, 52.0 - y)
        print "Getting", x, "cards of same suit", P
