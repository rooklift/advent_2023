# Enums for the various hand types, numbered by strength:

FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
PAIR = 2
NOTHING = 1

card_comparison_dict = {
	"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9,
	"8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

def parse(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f.read().split("\n") if line.strip() != ""]
	return [Hand(*line.split()) for line in lines]

class Hand:

	def __init__(self, cards, bid):
		self.cards = cards
		self.bid = int(bid)

	def strength(self):		# returns a number from 1 to 7, 7 being the strongest

		d = dict()
		for c in self.cards:
			try:
				d[c] += 1
			except KeyError:
				d[c] = 1

		if len(d) == 1:
			return FIVE_OF_A_KIND
		elif len(d) == 2:
			if max(d.values()) == 4:
				return FOUR_OF_A_KIND
			else:
				return FULL_HOUSE
		elif len(d) == 3:
			if max(d.values()) == 3:
				return THREE_OF_A_KIND
			else:
				return TWO_PAIR
		elif len(d) == 4:
			return PAIR
		elif len(d) == 5:
			return NOTHING
		else:
			raise ValueError

	def __lt__(self, other):

		if self.strength() < other.strength():
			return True
		if self.strength() > other.strength():
			return False

		for i in range(5):
			if card_comparison_dict[self.cards[i]] < card_comparison_dict[other.cards[i]]:
				return True
			if card_comparison_dict[self.cards[i]] > card_comparison_dict[other.cards[i]]:
				return False

		return False

def main():

	hands = parse("07_input.txt")
	hands = sorted(hands)

	result = 0
	for i, hand in enumerate(hands):
		result += hand.bid * (i + 1)

	print(result)


main()
