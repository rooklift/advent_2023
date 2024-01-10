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
	s = s.replace(">", ".")
	s = s.replace("v", ".")
	lines = [line.strip() for line in s.split("\n") if line.strip() != ""]
	width = len(lines[0])
	height = len(lines)
	world = make_2d_array(width, height)
	for x in range(width):
		for y in range(height):
			world[x][y] = lines[y][x]
	return world

class Connection:
	def __init__(self, dist, target):
		self.dist = dist
		self.target = target

	def __repr__(self):
		return "{} --> {},{}".format(self.dist, self.target.x, self.target.y)

class Node:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.connections = []
		self.start = False
		self.finish = False

	def fill_connections(self, world, nodes):
		for neighbour in neighbours(world, self.x, self.y):
			been = set()
			been.add((self.x, self.y))
			self.connections.append(get_connection(world, nodes, neighbour[0], neighbour[1], 1, been))

	def set_start_finish(self, world):
		if self.x == 1 and self.y == 0:
			self.start = True
		if self.x == len(world) - 2 and self.y == len(world[0]) - 1:
			self.finish = True

def neighbours(world, x, y):			# Only neighbours that are traversable i.e. "."
	ret = []
	for vector in vectors:
		x2, y2 = x + vector[0], y + vector[1]
		try:
			if world[x2][y2] == ".":
				ret.append((x2, y2))
		except IndexError:
			pass
	return ret

def is_node(world, x, y):
	if x == 1 and y == 0:
		return True
	if x == len(world) - 2 and y == len(world) - 1:
		return True
	if world[x][y] != ".":
		return False
	if len(neighbours(world, x, y)) > 2:
		return True
	return False

def get_connection(world, nodes, x, y, dist, been):

	# Initial call should be one step away from the node, with been set for it and dist == 1

	while True:

		been.add((x, y))

		if is_node(world, x, y):
			for node in nodes:
				if node.x == x and node.y == y:
					return Connection(dist, node)
			assert(False)

		neighs = neighbours(world, x, y)
		assert(len(neighs) == 2)

		for neighbour in neighs:
			if neighbour in been:
				continue
			x, y = neighbour
			dist += 1

def main():

	world = parse("23_input.txt")

	width = len(world)
	height = len(world[0])

	nodes = []

	for x in range(width):
		for y in range(height):
			if is_node(world, x, y):
				nodes.append(Node(x, y))

	for node in nodes:
		node.fill_connections(world, nodes)
		node.set_start_finish(world)

	search(nodes, width, height)

def search(nodes, width, height):

	for node in nodes:
		if node.start:
			start = node
			break

	search_recurse(start, 0, set())


best = 0


def search_recurse(node, dist, been):

	global best

	been = been.copy()
	been.add(node)

	for connection in node.connections:

		if connection.target in been:
			continue

		elif connection.target.finish:
			dist += connection.dist
			if dist > best:
				best = dist
			print(dist, best)
			continue

		else:
			search_recurse(connection.target, dist + connection.dist, been)


main()

