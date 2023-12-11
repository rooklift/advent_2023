def parse(filename):
	with open(filename) as f:
		return [line.strip() for line in f.read().split("\n") if line.strip() != ""]

def main(expansion):
	lines = parse("11_input.txt")
	big_cols = []
	big_rows = []
	galaxies = []

	for y, line in enumerate(lines):
		if "#" not in line:
			big_rows.append(y)
		for x, c in enumerate(line):
			if c == "#":
				galaxies.append([x,y])

	for x in range(len(lines[0])):
		col = [line[x] for line in lines]
		if "#" not in col:
			big_cols.append(x)

	for galaxy in galaxies:
		xd = 0
		yd = 0
		for col in big_cols:
			if col < galaxy[0]:
				xd += 1
		for row in big_rows:
			if row < galaxy[1]:
				yd += 1
		galaxy[0] += xd * (expansion - 1)
		galaxy[1] += yd * (expansion - 1)

	total = 0

	for i in range(len(galaxies) - 1):
		for j in range(i + 1, len(galaxies)):
			total += abs(galaxies[i][0] - galaxies[j][0])
			total += abs(galaxies[i][1] - galaxies[j][1])

	print(total)

main(2)				# i.e. each empty line becomes 2
main(1000000)		# i.e. each empty line becomes 1000000
