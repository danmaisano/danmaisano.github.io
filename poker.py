
import random
from classes import deck

bicycle = deck.Deck()

class Player():
    bicycle = deck.Deck()
    def __init__(self,name,chips):
        self.deck = deck.Deck()
        self.hand = []
        self.chips = chips
        self.name = name
        while len(self.hand) < 5:
            random_card = random.choice(self.deck.cards)
            self.hand.append(random_card)
            self.deck.cards.remove(random_card)
        self.hand = sorted(self.hand, key=lambda card: (card.point_val, card.suit))
        hand_str = ""
        for card in self.hand:
            hand_str += str(card.card_info()) + " | "
        print(f"You have the hand: {hand_str}\nHand Value: {Hand_Value(self.hand).get_value()}")

    def deal_cards(self):
        while len(self.hand) < 5:
            random_card = random.choice(self.deck.cards)
            self.hand.append(random_card)
            self.deck.cards.remove(random_card)
        self.hand = sorted(self.hand, key=lambda card: (card.point_val, card.suit))

    def show_hand(self):
        hand_str = ""
        for card in self.hand:
            hand_str += str(card.card_info()) + " | "
        print(f"You have the hand: {hand_str}\nHand Value: {Hand_Value(self.hand).get_value()}")

    def win_chips(self):
        if Hand_Value(self.hand).get_value() == "Royal Flush":
            self.chips += 5000
        if Hand_Value(self.hand).get_value() == "Straight Flush":
            self.chips += 3000
        if Hand_Value(self.hand).get_value() == "Four of a Kind":
            self.chips += 2000
        if Hand_Value(self.hand).get_value() == "Full House":
            self.chips += 1000
        if Hand_Value(self.hand).get_value() == "Flush":
            self.chips += 750
        if Hand_Value(self.hand).get_value() == "Straight":
            self.chips += 500
        if Hand_Value(self.hand).get_value() == "Three of a Kind":
            self.chips += 300
        if Hand_Value(self.hand).get_value() == "Two Pair":
            self.chips += 200
        if Hand_Value(self.hand).get_value() == "Pair":
            self.chips += 0
        if Hand_Value(self.hand).get_value() == "High Card":
            self.chips -= 100
        return self.chips
    
    def shuffle(self):
        self.deck = deck.Deck()
        return self.deck

class Hand_Value():
    def __init__(self, hand):
        self.hand = hand

    def get_value(self):
        if self.is_royal_flush():
            return ("Royal Flush") 
        elif self.is_straight_flush():
            return ("Straight Flush")
        elif self.is_four_of_a_kind():
            return ("Four of a Kind")
        elif self.is_full_house():
            return ("Full House")
        elif self.is_flush():
            return ("Flush")
        elif self.is_straight():
            return ("Straight")
        elif self.is_three_of_a_kind():
            return ("Three of a Kind")
        elif self.is_two_pair():
            return ("Two Pair")
        elif self.is_pair():
            return ("Pair")
        else:
            return ("High Card")

    def is_royal_flush(self):
        if self.is_straight_flush() and self.hand[0].point_val == 10:
            return True
    
    def is_straight_flush(self):
        if self.is_flush() and self.is_straight():
            return True

    def is_four_of_a_kind(self):
        for card in self.hand:
            count = 0
            for second_card in self.hand:
                if card.point_val == second_card.point_val:
                    count += 1
            if count == 4:
                return True
        
    def is_full_house(self):
        if self.is_three_of_a_kind() and self.is_pair():
            return True
        
    
    def is_flush(self):
        return all(card.suit == self.hand[0].suit for card in self.hand)

    def is_straight(self):
        return all(self.hand[i].point_val == self.hand[i-1].point_val + 1 for i in range(1, len(self.hand)))

    def is_three_of_a_kind(self):
        for card in self.hand:
            count = 0
            for second_card in self.hand:
                if card.point_val == second_card.point_val:
                    count += 1
            if count == 3:
                return True
    
    def is_two_pair(self):
        pair_count = 0
        for i in range(len(self.hand)):
            for j in range(i+1, len(self.hand)):
                if self.hand[i].point_val == self.hand[j].point_val:
                    pair_count += 1
        if pair_count == 2:
            return True

    def is_pair(self):
        counts = {}
        for card in self.hand:
            if card.point_val not in counts:
                counts[card.point_val] = 0
            counts[card.point_val] += 1
        return 2 in counts.values()

    def is_high_card(self):
        return True
