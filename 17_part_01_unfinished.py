def parse(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f.readlines() if line.strip() != ""]
		return Map(lines)

class Map:

	def __init__(self, lines):
		self.width = len(lines[0])
		self.height = len(lines)
		self.grid = [[] for c in lines[0]]
		for line in lines:
			for x, c in enumerate(line):
				self.grid[x].append(c)

def main():
	m = parse("17_input.txt")


main()
