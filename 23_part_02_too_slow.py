vectors = [
	(0, -1),
	(1, 0),
	(0, 1),
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
	s = s.replace("v", ".")
	s = s.replace(">", ".")
	lines = [line.strip() for line in s.split("\n") if line.strip() != ""]
	width = len(lines[0])
	height = len(lines)
	world = make_2d_array(width, height)
	for x in range(width):
		for y in range(height):
			world[x][y] = lines[y][x]
	world[-2][-1] = "F"
	return world

def main():
	world = parse("23_example.txt")
	been = set()
	been.add((1, 0))
	print("\nBest:", longest(world, 1, 1, 1, been))		# Cheap hack - start after 1 step made, at [1,1]

def longest(world, x, y, steps, been):

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

			if c == ".":
				valid_next_locs.append((px, py))
			elif c == "F":
				print(steps + 1)
				return steps + 1

		if len(valid_next_locs) == 0:
			return None
		elif len(valid_next_locs) == 1:
			steps += 1
			x = valid_next_locs[0][0]
			y = valid_next_locs[0][1]
			continue
		else:
			best = None
			for loc in valid_next_locs:
				dist = longest(world, loc[0], loc[1], steps + 1, been)
				if dist != None and (best == None or dist > best):
					best = dist
			return best


main()
