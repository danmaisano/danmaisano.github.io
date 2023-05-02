from . import deck
from . import hand_value
import random

bicycle = deck.Deck()


class Player():
    def __init__(self, chips):
        self.hand = []
        self.chips = chips

    def deal_cards(self):
        while len(self.hand) < 5:
            random_card = random.choice(bicycle.cards)
            self.hand.append(random_card)
            del bicycle[random_card]
        self.hand = sorted(self.hand, key=lambda card: (card.point_val, card.suit))

    def show_hand(self):
        hand_str = ""
        for card in self.hand:
            hand_str += str(card.card_info()) + " | "
        print(hand_str)

    def get_best_hand_value(self):
        hand_value = hand_value.Hand_Value(self.hand)
        return hand_value.get_value()

    def show_best_hand_value(self):
        print(f"Best hand value: {self.get_best_hand_value()}")

