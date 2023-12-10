# Whether we can move in this direction from the current square,
# assuming the receiving pipe allows it...

up = ["L", "|", "J", "S"]
down = ["F", "|", "7", "S"]
left = ["7", "-", "J", "S"]
right = ["F", "-", "L", "S"]

def parse(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f.read().split("\n") if line.strip() != ""]
		return Map(lines)

class Map:

	def __init__(self, lines):
		self.width = len(lines[0])
		self.height = len(lines)
		self.grid = [[] for c in lines[0]]
		for line in lines:
			for x, c in enumerate(line):
				self.grid[x].append(c)

	def get_s_loc(self):
		for x in range(self.width):
			for y in range(self.height):
				if self.grid[x][y] == "S":
					return x, y
		raise AssertionError

	def can_go_left(self, x, y):
		if x <= 0:
			return False
		if self.grid[x][y] in left and self.grid[x - 1][y] in right:
			return True
		return False

	def can_go_right(self, x, y):
		if x >= self.width - 1:
			return False
		if  self.grid[x][y] in right and self.grid[x + 1][y] in left:
			return True
		return False

	def can_go_up(self, x, y):
		if y <= 0:
			return False
		if  self.grid[x][y] in up and self.grid[x][y - 1] in down:
			return True
		return False

	def can_go_down(self, x, y):
		if y >= self.height - 1:
			return False
		if  self.grid[x][y] in down and self.grid[x][y + 1] in up:
			return True
		return False

	def loop_length(self):
		x, y = self.get_s_loc()
		visited = set()
		visited.add((x, y))
		while True:
			if self.can_go_left(x, y) and (x - 1, y) not in visited:
				x -= 1
			elif self.can_go_right(x, y) and (x + 1, y) not in visited:
				x += 1
			elif self.can_go_up(x, y) and (x, y - 1) not in visited:
				y -= 1
			elif self.can_go_down(x, y) and (x, y + 1) not in visited:
				y += 1
			else:									# Can't move because reached start
				return len(visited)
			visited.add((x, y))

def main():
	m = parse("10_input.txt")
	print(m.loop_length() // 2)

main()
