__author__ = 'saipc'
from Deck import Deck
# This pgm calculates the probability
# of getting a blackjack, with no prior
# info, and no memory

if __name__ == '__main__':
    # no jokers in bj, so this is fine
    deck = Deck()

    # Lets do one deck, easier to count,
    # and can replicate
    # We might need a separate card
    # counter class :)