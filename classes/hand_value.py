class Hand_Value():
    def __init__(self, hand):
        self.hand = hand

    def get_value(self):
        if self.is_royal_flush():
            print("Royal Flush")
            return 10
        elif self.is_straight_flush():
            print("Straight Flush")
            return 9
        elif self.is_four_of_a_kind():
            print("Four of a Kind")
            return 8
        elif self.is_full_house():
            print("Full House")
            return 7
        elif self.is_flush():
            print("Flush")
            return 6
        elif self.is_straight():
            print("Straight")
            return 5
        elif self.is_three_of_a_kind():
            print("Three of a Kind")
            return 4
        elif self.is_two_pair():
            print("Two Pair")
            return 3
        elif self.is_pair():
            print("Pair")
            return 2
        else:
            print("High Card")
            return 1

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
        for card in self.hand:
            if self.hand.count(card) == 2:
                return True

    def is_high_card(self):
        return True

    # def __gt__(self, other):
    #     return self.get_value() > other.get_value()

    # def __eq__(self, other):
    #     return self.get_value() == other.get_value()

    # def __lt__(self, other):
    #     return self.get_value() < other.get_value()

    def show_hand_value(self):
        print(f"Hand value: {self.get_value()}")
