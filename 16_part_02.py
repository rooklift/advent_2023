def parse(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f.read().split("\n") if line.strip() != ""]
		return Map(lines)

N = 1
E = 2
S = 3
W = 4

RULES = {
	N: {"|":  [N],
		"-":  [W, E],
		"/":  [E],
		"\\": [W]},

	E: {"|":  [N, S],
		"-":  [E],
		"/":  [N],
		"\\": [S]},

	S: {"|":  [S],
		"-":  [W, E],
		"/":  [W],
		"\\": [E]},

	W: {"|":  [N, S],
		"-":  [W],
		"/":  [S],
		"\\": [N]}
}

VECTORS = {
	N: (0, -1),
	E: (1, 0),
	S: (0, 1),
	W: (-1, 0)
}

class Map:
	def __init__(self, lines):
		self.width = len(lines[0])
		self.height = len(lines)
		self.map = []
		self.light = []
		for x in range(self.width):
			self.map.append([])
			self.light.append([])
		for y in range(self.height):
			for x in range(self.width):
				c = lines[y][x]
				self.map[x].append(c)
				self.light[x].append(set())

	def propagate(self, x, y, direction, todo):
		if x < 0 or x >= self.width or y < 0 or y >= self.height:
			return
		if direction in self.light[x][y]:
			return
		self.light[x][y].add(direction)
		if self.map[x][y] == ".":
			next_dirs = [direction]
		else:
			next_dirs = RULES[direction][self.map[x][y]]
		for d in next_dirs:
			vector = VECTORS[d]
			next_x = x + vector[0]
			next_y = y + vector[1]
			todo.add((next_x, next_y, d))
		return

	def reset(self):
		for x in range(self.width):
			for y in range(self.height):
				self.light[x][y] = set()

	def count_energy(self):
		ret = 0
		for x in range(self.width):
			for y in range(self.height):
				if len(self.light[x][y]) > 0:
					ret += 1
		return ret

def main():
	m = parse("16_input.txt")
	results = []
	for x in range(m.width):
		results.append(work(m, x, 0, S))
		results.append(work(m, x, m.height - 1, N))
	for y in range(m.height):
		results.append(work(m, 0, y, E))
		results.append(work(m, m.width - 1, y, W))
	print(max(results))

def work(m, x, y, direction):
	m.reset()
	todo = set()
	todo.add((x, y, direction))
	while len(todo) > 0:
		x, y, direction = todo.pop()
		m.propagate(x, y, direction, todo)
	return m.count_energy()

main()