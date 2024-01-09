# Note: I believe the input is setup so it's never possible to enter a loop.

N = 1
E = 2
S = 3
W = 4

permitted_next = {
	N: [N, E, W],
	E: [E, S, N],
	S: [S, W, E],
	W: [W, N, S]
}

permitted_tiles = {
	N: ["."],
	E: [".", ">"],
	S: [".", "v"],
	W: ["."]
}

vectors = {
	N: [0, -1],
	E: [1, 0],
	S: [0, 1],
	W: [-1, 0]
}

def make_2d_array(width, height):
	ret = []
	for x in range(width):
		ret.append([])
		for y in range(height):
			ret[x].append(None)
	return ret

def parse(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f.read().split("\n") if line.strip() != ""]
	width = len(lines[0])
	height = len(lines)
	world = make_2d_array(width, height)
	for x in range(width):
		for y in range(height):
			world[x][y] = lines[y][x]
	world[-2][-1] = "F"
	return world

def main():
	world = parse("23_input.txt")
	print(longest(world, 1, 0, S, 0))

def longest(world, x, y, direction, steps):

	while True:

		possible_next_dirs = permitted_next[direction]

		valid_next_locs = []
		valid_next_dirs = []

		for pnd in possible_next_dirs:

			vector = vectors[pnd]

			px = x + vector[0]
			py = y + vector[1]

			c = world[px][py]

			if c in permitted_tiles[pnd]:
				valid_next_locs.append((px, py))
				valid_next_dirs.append(pnd)

		if len(valid_next_locs) == 0:		# We reached F
			return steps + 1
		elif len(valid_next_locs) == 1:
			steps += 1
			x = valid_next_locs[0][0]
			y = valid_next_locs[0][1]
			direction = valid_next_dirs[0]
			continue
		else:
			best = 0
			for i, loc in enumerate(valid_next_locs):
				dist = longest(world, loc[0], loc[1], valid_next_dirs[i], steps + 1)
				if dist > best:
					best = dist
			return best


main()
