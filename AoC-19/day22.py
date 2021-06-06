class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Deck:
    def __init__(self, size):
        self.cards = []
        self.i = 0
        self.direction = 1

        for value in range(size):
            self.cards.append(value)

    def __iter__(self):
        for _ in range(len(self.cards)):
            result = self.cards[self.i]
            self.i = (self.i + self.direction) % len(self.cards)
            yield result

    def __str__(self):
        string = "["
        for card in self:
            string += str(card) + ","
        return string[:-1] + "]"

    def deal_to_new_stack(self):
        self.i = (self.i + len(self.cards) - self.direction) % len(self.cards)
        self.direction = -self.direction

    def cut(self, count):
        self.i = (self.i + len(self.cards) + count * self.direction) % len(self.cards)

    def deal_with_increment(self, inc):
        new_cards = [0] * len(self.cards)
        i_new = 0
        
        for card in self:
            new_cards[i_new] = card
            i_new = (i_new + inc + len(self.cards)) % len(self.cards)

        self.cards = new_cards
        self.i = 0
        self.direction = 1

    def get_value_at_index(self, index):
        return self.cards[(self.i + index * self.direction + len(self.cards)) % len(self.cards)]

    def get_position_of_card(self, card_to_find):
        i_pos = 0
        for card_in_deck in self:
            if card_in_deck == card_to_find:
                return i_pos
            i_pos += 1
        raise Exception("Card not in deck.")

f = open("data.txt")
data = [i.split() for i in f.read().split("\n")]
f.close()

deck = Deck(41)

print(deck)

deck.deal_with_increment(3)
print(deck)
deck.deal_with_increment(3)
print(deck)
deck.deal_with_increment(3)
print(deck)
deck.deal_with_increment(3)
print(deck)
deck.deal_with_increment(3)
print(deck)
deck.deal_with_increment(3)
print(deck)
deck.deal_with_increment(3)
print(deck)
deck.deal_with_increment(3)
print(deck)
deck.deal_with_increment(3)
print(deck)
# for tech in data:
#     if tech[1] == "with":
#         deck.deal_with_increment(int(tech[3]))
#         output = "inc"+ tech[3]+": "
#     elif tech[1] == "into":
#         deck.deal_to_new_stack()
#         output = "deal: "
#     else:
#         deck.cut(int(tech[1]))
#         output = "cut"+ tech[1]+":" + (" " if int(tech[1]) >= 0 else "")

# print(deck.get_position_of_card(2019))