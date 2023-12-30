def parse(filename):
	with open(filename) as f:
		return [line.strip() for line in f.read().split("\n") if line.strip() != ""]

def main():

	lines = parse("21_input.txt")

	empty = set()		# Spaces we can go to.
	blocked = set()		# Walls. This is not really used.

	results = []

	for n in range(65):
		results.append(set())

	for y in range(len(lines)):
		for x in range(len(lines[0])):
			if lines[y][x] == ".":
				empty.add((x, y))
			elif lines[y][x] == "#":
				blocked.add((x, y))
			elif lines[y][x] == "S":
				results[0].add((x, y))

	for n in range(64):		# Not 65

		for x, y in results[n]:

			if (x - 1, y) in empty:
				results[n + 1].add((x - 1, y))
				empty.discard((x - 1, y))

			if (x + 1, y) in empty:
				results[n + 1].add((x + 1, y))
				empty.discard((x + 1, y))

			if (x, y - 1) in empty:
				results[n + 1].add((x, y - 1))
				empty.discard((x, y - 1))

			if (x, y + 1) in empty:
				results[n + 1].add((x, y + 1))
				empty.discard((x, y + 1))

	total = 0

	for i in range(0, 65, 2):
		total += len(results[i])

	print(total)


main()
