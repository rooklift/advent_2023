with open("21_input.txt") as f:
	lines = [line.strip() for line in f.read().split("\n") if line.strip() != ""]

empty = set()		# Spaces we can go to.

results = [set() for n in range(65)]

for y in range(len(lines)):
	for x in range(len(lines[0])):
		if lines[y][x] == ".":
			empty.add((x, y))
		elif lines[y][x] == "S":
			results[0].add((x, y))

for n in range(64):				# Not 65
	for x, y in results[n]:
		for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
			if (x + i, y + j) in empty:
				results[n + 1].add((x + i, y + j))
				empty.discard((x + i, y + j))

total = 0

for i in range(0, 65, 2):
	total += len(results[i])

print(total)
