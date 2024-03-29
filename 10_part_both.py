# Strategy for Part 2:
# Traverse the loop
# Clear all non-loop spots to be dots, i.e. "."
# Now traverse the loop again:
#	If a dot is seen on the LEFT (from the POV of the traversal) flag it (convert it to " ")
# Flood fill the flags through the dots
# The flags are either all of the outside locations, or all of the inside locations
#
# -------------------------------------------------------------------------------------------------

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

	def shrink(self):
		# Decrease width...
		self.grid = self.grid[1:-1]
		self.width -= 2
		# Decrease height...
		self.grid = [col[1:-1] for col in self.grid]
		self.height -= 2

	def can_go_left(self, x, y):
		return self.grid[x][y] in LEFT and self.grid[x - 1][y] in RIGHT

	def can_go_right(self, x, y):
		return self.grid[x][y] in RIGHT and self.grid[x + 1][y] in LEFT

	def can_go_up(self, x, y):
		return self.grid[x][y] in UP and self.grid[x][y - 1] in DOWN

	def can_go_down(self, x, y):
		return self.grid[x][y] in DOWN and self.grid[x][y + 1] in UP

	def loop(self, r):				# In round 1, non-loop parts of the grid get made into "."
									# In round 2, dots on the LEFT are converted to " "
		x, y = self.get_s_loc()
		visited = set()
		visited.add((x, y))
		while True:
			if self.can_go_left(x, y) and (x - 1, y) not in visited:
				if r == 2:
					if self.grid[x][y + 1] == ".":
						self.grid[x][y + 1] = " "
					if self.grid[x - 1][y + 1] == ".":
						self.grid[x - 1][y + 1] = " "
				x -= 1
			elif self.can_go_right(x, y) and (x + 1, y) not in visited:
				if r == 2:
					if self.grid[x][y - 1] == ".":
						self.grid[x][y - 1] = " "
					if self.grid[x + 1][y - 1] == ".":
						self.grid[x + 1][y - 1] = " "
				x += 1
			elif self.can_go_up(x, y) and (x, y - 1) not in visited:
				if r == 2:
					if self.grid[x - 1][y] == ".":
						self.grid[x - 1][y] = " "
					if self.grid[x - 1][y - 1] == ".":
						self.grid[x - 1][y - 1] = " "
				y -= 1
			elif self.can_go_down(x, y) and (x, y + 1) not in visited:
				if r == 2:
					if self.grid[x + 1][y] == ".":
						self.grid[x + 1][y] = " "
					if self.grid[x + 1][y + 1] == ".":
						self.grid[x + 1][y + 1] = " "
				y += 1
			else:											# Can't move because reached start
				break
			visited.add((x, y))
		if r == 1:
			for x in range(self.width):
				for y in range(self.height):
					if (x, y) not in visited:
						self.grid[x][y] = "."
		return len(visited)

	def neighbours(self, x, y):
		return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

	def flood(self):		# Every dot that touches a " " needs to become " "
		todo = set()
		for x in range(self.width):
			for y in range(self.height):
				if self.grid[x][y] == " ":
					todo.add((x, y))
		while True:
			new_todo = set()
			for (x, y) in todo:
				neighbours = self.neighbours(x, y)
				for (nx, ny) in neighbours:
					if self.grid[nx][ny] == ".":
						self.grid[nx][ny] = " "
						new_todo.add((nx, ny))
			if len(new_todo) == 0:
				return
			todo = new_todo

	def string(self):
		lines = []
		for y in range(self.height):
			line = []
			for x in range(self.width):
				line.append(self.grid[x][y])
			lines.append("".join(line))
		return "\n".join(lines)

def main():

	m = parse("10_input.txt")

	m.add_border()				# Avoid literal edge cases
	tubes = m.loop(1)
	m.loop(2)
	m.flood()
	m.shrink()					# Undo the expansion (add_border) above

	left_count = m.string().count(" ")
	right_count = m.string().count(".")

	print(m.string())
	print("     Tubes:", tubes)
	print("       / 2:", tubes // 2, "  (this answers part 1)")
	print(" Left side:", left_count)
	print("Right side:", right_count)
	print("     Total:", tubes + left_count + right_count)


main()
