class Number:
	def __init__(self, val, x, y):		# x is the x-location of the FINAL digit in the number
		self.val = val
		self.x = x
		self.y = y
	def search_range(self):				# returns half-open [range) values appropriate to pass to the range() function
		x1 = self.x - len(str(self.val))
		x2 = self.x + 2
		y1 = self.y - 1
		y2 = self.y + 2
		return x1, y1, x2, y2
	def adjust_stars(self, lines, star_dict):
		x1, y1, x2, y2 = self.search_range()
		for y in range(y1, y2):
			for x in range(x1, x2):
				if lines[y][x] == "*":	# Note [y][x] order
					star_dict[(x, y)].nums.append(self.val)

class Star:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.nums = []
	def value(self):
		if len(self.nums) != 2:
			return 0
		return self.nums[0] * self.nums[1]

def nice_lines(filename):
	with open(filename) as f:
		return [line.strip() for line in f.readlines() if line.strip() != ""]

def add_border(lines):					# adds a border of dots all around to prevent edge cases...
	adjusted_lines = []
	for line in lines:
		adjusted_lines.append(".{}.".format(line))
	empty_line = "." * len(adjusted_lines[0])
	return [empty_line] + adjusted_lines + [empty_line]

def make_nums(lines):
	all_nums = []
	for y, line in enumerate(lines):
		acc = 0
		for x, c in enumerate(line):
			if c.isdigit():
				acc *= 10
				acc += int(c)
			else:
				if acc > 0:
					all_nums.append(Number(acc, x - 1, y))
					acc = 0
	return all_nums

def make_stars(lines):					# dict of (x, y) --> Star object
	star_dict = dict()
	for y, line in enumerate(lines):
		for x, c in enumerate(line):
			if c == "*":
				star_dict[(x, y)] = Star(x, y)
	return star_dict

def main():
	lines = add_border(nice_lines("03_input.txt"))
	all_nums = make_nums(lines)
	star_dict = make_stars(lines)
	for num in all_nums:
		num.adjust_stars(lines, star_dict)
	print(sum(star.value() for star in star_dict.values()))

main()
