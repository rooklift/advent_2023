def nice_lines(filename):
	with open(filename) as f:
		return [line.strip() for line in f.readlines() if line.strip() != ""]

def main():
	lines = nice_lines("04_input.txt")

	# Note: we'll ignore the id numbers given to us and label the cards from 0 instead.

	counts = [1 for line in lines]

	for i, line in enumerate(lines):
		tokens1 = line.split(":")[1].split("|")[0].split()
		tokens2 = line.split(":")[1].split("|")[1].split()
		set1 = set(tokens1)
		set2 = set(tokens2)
		creations = len(set1.intersection(set2))

		for n in range(i + 1, i + 1 + creations):
			counts[n] += counts[i]

	print(sum(counts))

main()
