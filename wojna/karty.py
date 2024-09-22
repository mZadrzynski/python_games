#gra w karty
#demonstruje tworzenie kombinacji obiektow


class Card(object):
    """karta do gry"""
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["c", "d", "h", "s"]
    CARD_VALUES = {
        "2": 2,
        "3": 3, 
        "4": 4, 
        "5": 5, 
        "6": 6, 
        "7": 7, 
        "8": 8, 
        "9": 9, 
        "10": 10, 
        "J": 11, 
        "Q": 12, 
        "K": 13, 
        "A": 14
    }

    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def card_value(self):
        return self.value

    def __str__(self):
        rep = self.rank + self.suit + " v: " + str(self.value)
        return rep
    
class Hand(object):
    """reka, karty do gry w reku"""
    def __init__(self):
        self.cards = []

    
    def __len__(self):
        return len(self.cards)


    def __str__(self):
        if self.cards:
            rep = "" + "dlugosc tali =" + str(len(self.cards)) + " karty to: \n"
            for card in self.cards:
                rep += str(card) + " " 
        else:
            rep = "<pusta>"
        return rep
    
    def __getitem__(self, index):
        return self.cards[index]
    
    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)
    
    def append(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    def remove(self, card):
        try:
            self.cards.remove(card)
        except ValueError:
            print(f"Card {card} not found in hand.")
    
    def len(self):
        return len(self.cards)
    
    def suffle(self):
        import random
        random.shuffle(self.cards)

class Deck(Hand):
    """talia do kart"""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit, value = Card.CARD_VALUES[rank]))

    def suffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("nie moge dalej rozdawac zabraklo kard")
    
if __name__ == "__main__":
    print("to modul zawierajacy klasy do gry w karty")
    input("\n aby zakonczyc nacisnij klawisz enter")


# my_hand = Hand()
# deck1 = Deck()
# deck1.populate()
# deck1.suffle()

# hands = [my_hand]
# print(deck1)
# deck1.deal(hands, per_hand=1)

# print("moja reka posaiada: ")
# print(my_hand.cards[0].card_value())