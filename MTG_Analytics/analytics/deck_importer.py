import path
from collections import namedtuple


Deck = namedtuple('Deck', 'name maindeck sideboard')


class DeckImporter:

    def __init__(self, decks_folder):
        self.decks = []
        pass

    def parse_decklist(self, decklist):
        # read file: first line is the deck's name, followed by a blank line,
        # followed by the decklist (must be at least 60 cards), followed by
        # another blank line, followed by the sideboard (exactly 15 cards).
        # Separate the maindeck from the sideboard and verify they are valid
        name = line.read()  # skip to the next nonblank line

        info = line.read()
        d = {}
        while info is not empty:
            count, cardname = line.split()
            d[cardname] += count
            info = line.read()
        assert sum(v for _, v in d) >= 60

        info = line.read()
        s = {}
        while info is not empty:
            count, cardname = line.split()
            s[cardname] += count
            info = line.read()
        assert sum(v for _, v in d) == 15

        self.decks.append(Deck(name, d, s))
