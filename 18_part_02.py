# Pretty pleased with this one, I got it all by myself while other people
# were looking up the Shoelace Formula and Pick's Theorem and such.
# My approach is quite different.

import itertools

VECTORS = {
	"U": (0, -1),
	"D": (0, 1),
	"L": (-1, 0),
	"R": (1, 0)
}

DIRECTIONS = {
	"0": "R",
	"1": "D",
	"2": "L",
	"3": "U",
}

def parse(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f.readlines() if line.strip() != ""]
	ret = []
	for line in lines:
		_, _, colour = line.split()
		dist = int(colour[2:7], 16)
		udlr = DIRECTIONS[colour[7]]
		ret.append((udlr, dist))
	return ret

def get_vertical_edges(vals):
	edges = []
	x = 0
	y = 0
	for val in vals:
		old_y = y
		direction = val[0]
		x += VECTORS[direction][0] * val[1]
		y += VECTORS[direction][1] * val[1]
		if direction in ["U", "D"]:
			edges.append(Edge(x, old_y, x, y))
	return edges

class Edge:

	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		if self.x1 > self.x2:
			self.x1, self.x2 = self.x2, self.x1
		if self.y1 > self.y2:
			self.y1, self.y2 = self.y2, self.y1
		if self.x1 != self.x2 and self.y1 != self.y2:		# We only accept straight edges
			raise ValueError

class Rect:

	def __init__(self, x1, y1, x2, y2):						# note x2, y2 are included in the rect
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		if self.x1 > self.x2:
			self.x1, self.x2 = self.x2, self.x1
		if self.y1 > self.y2:
			self.y1, self.y2 = self.y2, self.y1

	def area(self):
		return (self.x2 + 1 - self.x1) * (self.y2 + 1 - self.y1)

	def overlap(self, other):
		# https://stackoverflow.com/questions/27152904/calculate-overlapped-area-between-two-rectangles
		dx = min(self.x2 + 1, other.x2 + 1) - max(self.x1, other.x1)
		dy = min(self.y2 + 1, other.y2 + 1) - max(self.y1, other.y1)
		if dx >= 0 and dy >= 0:
			return dx * dy
		else:
			return 0

def main():

	# The basic idea is to divide the thing into rectangles then work out the overall area.

	vals = parse("18_input.txt")
	vedges = get_vertical_edges(vals)

	significant_y_vals = set()		# Any y where an edge starts or ends.
	for edge in vedges:
		significant_y_vals.add(edge.y1)
		significant_y_vals.add(edge.y2)
	significant_y_vals = sorted(list(significant_y_vals))

	rects = []

	for i in range(len(significant_y_vals) - 1):

		y1 = significant_y_vals[i]
		y2 = significant_y_vals[i + 1]

		# Find the x of all lines that fully include (y1,y2)...

		x_vals = [edge.x1 for edge in vedges if edge.y1 <= y1 and edge.y2 >= y2]
		x_vals.sort()

		# Construct the rects that are inside the loop...

		top_edges = [Edge(x_vals[i], y1, x_vals[i + 1], y1) for i in range(0, len(x_vals), 2)]

		for top in top_edges:
			rects.append(Rect(top.x1, y1, top.x2, y2))

	area = sum([rect.area() for rect in rects])

	excess = 0
	overlap_count = 0

	# Test every possible pair of rects. Really we should just test each row of rects created
	# against the next row of rects created...

	for combo in itertools.combinations(rects, 2):
		ov = combo[0].overlap(combo[1])
		if ov > 0:
			excess += ov
			overlap_count += 1

	print("   rects:", len(rects))
	print("overlaps:", overlap_count)
	print("   naive:", area)
	print("  excess:", excess)
	print("  result:", area - excess)

main()
