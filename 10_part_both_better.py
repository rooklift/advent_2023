# Which pipe types can connect in which directions? Note S is special and could go any direction.
# Whether the pipe actually connects depends on whether the pipe it is trying to connect to can connect to it.

UP = ["L", "|", "J", "S"]
DOWN = ["F", "|", "7", "S"]
LEFT = ["7", "-", "J", "S"]
RIGHT = ["F", "-", "L", "S"]

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

	def add_border(self):
		# Increase width...
		self.grid.insert(0, ["."] * self.height)
		self.grid.append(["."] * self.height)
		self.width += 2
		# Increase height...
		for x in range(self.width):
			self.grid[x].insert(0, ".")
			self.grid[x].append(".")
		self.height += 2

	def can_go_left(self, x, y):
		return self.grid[x][y] in LEFT and self.grid[x - 1][y] in RIGHT

	def can_go_right(self, x, y):
		return self.grid[x][y] in RIGHT and self.grid[x + 1][y] in LEFT

	def can_go_up(self, x, y):
		return self.grid[x][y] in UP and self.grid[x][y - 1] in DOWN

	def can_go_down(self, x, y):
		return self.grid[x][y] in DOWN and self.grid[x][y + 1] in UP

	def loop(self):							# Return amount of tubing. Also sets all non-tube spots to "."
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
			else:							# Can't move because reached start
				break
			visited.add((x, y))
		for x in range(self.width):
			for y in range(self.height):
				if (x, y) not in visited:
					self.grid[x][y] = "."
		return len(visited)

	def count_inside(self):					# Each time we cross a tube, we go from inside to outside or vice versa
		total = 0
		for y in range(self.height):
			inside = False
			entry = None					# What piece we entered a horizontal stretch of tube via (one of F L)
			for x in range(self.width):
				c = self.grid[x][y]
				if c == ".":
					if inside:
						total += 1
				elif c == "|":
					inside = not inside
				elif c == "-":
					pass					# "-" i.e. horizontal pipe neither adds to the total nor changes our inside/outside status
				elif c == "F":
					entry = "F"
				elif c == "L":
					entry = "L"
				elif c == "7":
					if entry == "L":
						inside = not inside
				elif c == "J":
					if entry == "F":
						inside = not inside
		return total

def main():
	m = parse("10_input.txt")
	m.add_border()							# Avoid literal edge cases
	tubes = m.loop()
	inside = m.count_inside()
	print("Maximum distance: ", tubes // 2)
	print("    Space inside: ", inside)


main()
