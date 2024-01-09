vectors = [
	(0, -1),
	(0, 1),
	(1, 0),
	(-1, 0)
]

def make_2d_array(width, height):
	ret = []
	for x in range(width):
		ret.append([])
		for y in range(height):
			ret[x].append(None)
	return ret

def parse(filename):
	with open(filename) as f:
		s = f.read()
	lines = [line.strip() for line in s.split("\n") if line.strip() != ""]
	width = len(lines[0])
	height = len(lines)
	world = make_2d_array(width, height)
	for x in range(width):
		for y in range(height):
			world[x][y] = lines[y][x]
	world[-2][-1] = "F"
	return world

result = 0

def main():
	global result
	world = parse("23_input.txt")
	been = set()
	been.add((1, 0))
	search(world, 1, 1, 1, been)		# Cheap hack - start after 1 step made, at [1,1]
	print("Result:", result)

def search(world, x, y, steps, been):

	global result

	been = been.copy()

	while True:

		been.add((x, y))

		valid_next_locs = []

		for vector in vectors:

			px = x + vector[0]
			py = y + vector[1]

			if (px, py) in been:
				continue

			c = world[px][py]

			if c == "." or c == ">" or c == "v":
				valid_next_locs.append((px, py))
			elif c == "F":
				print(steps + 1, result)
				if steps + 1 > result:
					result = steps + 1
				return

		if len(valid_next_locs) == 0:
			return
		elif len(valid_next_locs) == 1:
			steps += 1
			x = valid_next_locs[0][0]
			y = valid_next_locs[0][1]
			continue
		elif x == 131 and y == 125:		# Stupid optimisation
			steps += 1
			x = 131
			y = 126
			continue
		else:
			for loc in valid_next_locs:
				search(world, loc[0], loc[1], steps + 1, been)
			return


main()
