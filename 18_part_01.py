VECTORS = {
	"U": (0, -1),
	"D": (0, 1),
	"L": (-1, 0),
	"R": (1, 0)
}

def parse(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f.readlines() if line.strip() != ""]
	ret = []
	for line in lines:
		udlr, dist, colour = line.split()
		colour = colour[2:8]
		ret.append((udlr, int(dist), colour))
	return ret

def get_bounds(vals):		# returns x1, y1, x2, y2
	x = 0
	y = 0
	all_x = []
	all_y = []
	for val in vals:
		direction = val[0]
		x += VECTORS[direction][0] * val[1]
		y += VECTORS[direction][1] * val[1]
		all_x.append(x)
		all_y.append(y)
	return min(all_x), min(all_y), max(all_x) + 1, max(all_y) + 1

def make_2d_array(width, height, defval):
	ret = []
	for x in range(width):
		ret.append([])
		for y in range(height):
			ret[x].append(defval)
	return ret

def neighbours(x, y):
	return (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)

def flood(grid, startx, starty, c):
	todo = [(startx, starty)]
	while len(todo) > 0:
		new_todo = []
		for point in todo:
			for neigh in neighbours(*point):
				try:
					if grid[neigh[0]][neigh[1]] == ".":
						grid[neigh[0]][neigh[1]] = c
						new_todo.append((neigh[0], neigh[1]))
				except IndexError:
					pass
		todo = new_todo

def count(grid, c):
	ret = 0
	for x in range(len(grid)):
		for y in range(len(grid[0])):
			if grid[x][y] == c:
				ret += 1
	return ret

def main():
	vals = parse("18_input.txt")
	x1, y1, x2, y2 = get_bounds(vals)
	grid = make_2d_array(x2 - x1, y2 - y1, ".")
	x = abs(x1)
	y = abs(y1)
	grid[x][y] = "#"
	for val in vals:
		direction = val[0]
		dist = val[1]
		for d in range(dist):
			x += VECTORS[direction][0]
			y += VECTORS[direction][1]
			grid[x][y] = "#"
	flood(grid, 0, 0, "?")
	print(count(grid, "#") + count(grid, "."))

main()
