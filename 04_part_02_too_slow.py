def nice_lines(filename):
	with open(filename) as f:
		return [line.strip() for line in f.readlines() if line.strip() != ""]

class Card:
	def __init__(self, line):
		self.line = line
	def num(self):
		return int(self.line.split(":")[0].split()[1])
	def count_creations(self):
		tokens1 = self.line.split(":")[1].split("|")[0].split()
		tokens2 = self.line.split(":")[1].split("|")[1].split()
		set1 = set(tokens1)
		set2 = set(tokens2)
		return len(set1.intersection(set2))
	def scratch(self):
		return range(self.num() + 1, self.num() + 1 + self.count_creations())
	def copy(self):
		return Card(self.line)		# Note: doesn't copy scratched status

def main():

	lines = nice_lines("04_example.txt")

	og_cards = [None]				# We won't actually touch these. We will start with copies.
	for line in lines:
		og_cards.append(Card(line))

	active_cards = []

	for card in og_cards[1:]:
		active_cards.append(card.copy())

	count = 0

	while True:

		if len(active_cards) == 0:
			break
		else:
			count += len(active_cards)

		new_cards = []

		for card in active_cards:
			new_card_nums = card.scratch()
			for num in new_card_nums:
				new_cards.append(og_cards[num].copy())

		active_cards = new_cards

	print(count)


main()
