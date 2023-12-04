def nice_lines(filename):
	with open(filename) as f:
		return [line.strip() for line in f.readlines() if line.strip() != ""]

class Card:
	def __init__(self, line):
		self.line = line
		self.num = int(self.line.split(":")[0].split()[1])
		self.creations = None		# Done next...
		self.make_creations()
	def make_creations(self):
		tokens1 = self.line.split(":")[1].split("|")[0].split()
		tokens2 = self.line.split(":")[1].split("|")[1].split()
		set1 = set(tokens1)
		set2 = set(tokens2)
		self.creations = list(range(self.num + 1, self.num + 1 + len(set1.intersection(set2))))

def main():

	lines = nice_lines("04_input.txt")

	og_cards = [None]				# We won't actually touch these. We will start with copies. The None exists to get correct indices.

	for line in lines:
		og_cards.append(Card(line))

	active_cards = []

	for card in og_cards[1:]:
		active_cards.append(card)

	count = 0

	while True:

		print(count)

		if len(active_cards) == 0:
			break
		else:
			count += len(active_cards)

		new_cards = []

		for card in active_cards:
			for num in card.creations:
				new_cards.append(og_cards[num])

		active_cards = new_cards

	print("Answer:")
	print(count)

main()
