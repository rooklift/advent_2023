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
		self.lines = lines				# Remember to use [y][x] when accessing
		self.width = len(lines[0])
		self.height = len(lines)
		self.light = set()

	def propagate(self, x, y, direction, todo):
		if x < 0 or x >= self.width or y < 0 or y >= self.height:
			return
		if (x, y, direction) in self.light:
			return
		self.light.add((x, y, direction))
		if self.lines[y][x] == ".":
			next_dirs = [direction]
		else:
			next_dirs = RULES[direction][self.lines[y][x]]
		for d in next_dirs:
			vector = VECTORS[d]
			next_x = x + vector[0]
			next_y = y + vector[1]
			todo.add((next_x, next_y, d))
		return

	def reset(self):
		self.light = set()

	def count_energy(self):
		energised = set()
		for x, y, _ in self.light:
			energised.add((x, y))
		return len(energised)


def parse(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f.read().split("\n") if line.strip() != ""]
		return Map(lines)

def work(m, x, y, direction):
	m.reset()
	todo = set()
	todo.add((x, y, direction))
	while len(todo) > 0:
		x, y, direction = todo.pop()
		m.propagate(x, y, direction, todo)
	return m.count_energy()

def main():
	m = parse("16_input.txt")
	results = []
	for y in range(m.height):
		results.append(work(m, 0, y, E))
		results.append(work(m, m.width - 1, y, W))
	for x in range(m.width):
		results.append(work(m, x, 0, S))
		results.append(work(m, x, m.height - 1, N))
	print(results[0])		# Part 1
	print(max(results))		# Part 2

main()
