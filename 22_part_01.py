def parse(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f.read().split("\n") if line.strip() != ""]
	ret = []
	for line in lines:
		params = [int(s) for s in line.replace("~", ",").split(",")]
		ret.append(Shape(*params))
	return ret

class Shape:

	def __init__(self, x1, y1, z1, x2, y2, z2):		# We can assume x1 <= x2 etc...
		self.blocks = []
		if x1 != x2:
			for x in range(x1, x2 + 1):
				self.blocks.append((x, y1, z1))
		elif y1 != y2:
			for y in range(y1, y2 + 1):
				self.blocks.append((x1, y, z1))
		elif z1 != z2:
			for z in range(z1, z2 + 1):
				self.blocks.append((x1, y1, z))
		else:
			self.blocks.append((x1, y1, z1))

	def min_z(self):
		return min([o[2] for o in self.blocks])

	def max_z(self):
		return max([o[2] for o in self.blocks])

	def is_vertical(self):
		return self.blocks[0][2] != self.blocks[-1][2]

	def spots_below(self):
		if self.is_vertical():
			return [(self.blocks[0][0], self.blocks[0][1], self.min_z() - 1)]
		else:
			ret = []
			for block in self.blocks:
				ret.append((block[0], block[1], block[2] - 1))
			return ret

	def spots_above(self):
		if self.is_vertical():
			return [(self.blocks[0][0], self.blocks[0][1], self.max_z() + 1)]
		else:
			ret = []
			for block in self.blocks:
				ret.append((block[0], block[1], block[2] + 1))
			return ret

	def has_supporters(self, block_dict):
		for spot in self.spots_below():
			if spot in block_dict:
				return True
		return False

	def remove_from_dict(self, d):
		for block in self.blocks:
			del d[block]

	def add_to_dict(self, d):
		for block in self.blocks:
			d[block] = self

	def drop(self, block_dict):
		self.remove_from_dict(block_dict)
		self.blocks = [(o[0], o[1], o[2] - 1) for o in self.blocks]
		self.add_to_dict(block_dict)

	def has_exactly_one_supporter(self, block_dict):
		supporters = set()
		for spot in self.spots_below():
			if spot in block_dict:
				supporters.add(block_dict[spot])
		return len(supporters) == 1

	def is_necessary(self, block_dict):		# Shape is necessary if it is the ONLY supporter of any shape
		supported_shapes = set()
		for block in self.spots_above():
			if block in block_dict:
				supported_shapes.add(block_dict[block])
		for shape in supported_shapes:
			if shape.has_exactly_one_supporter(block_dict):
				return True
		return False

def main():
	shapes = parse("22_input.txt")				# Array of shapes
	block_dict = dict()							# (x,y,z) --> shape
	for shape in shapes:
		shape.add_to_dict(block_dict)
	while True:
		did_work = False
		for shape in shapes:
			while not (shape.has_supporters(block_dict) or shape.min_z() == 1):
				shape.drop(block_dict)
				did_work = True
		if not did_work:
			break
	total_removable = 0
	for shape in shapes:
		needed = shape.is_necessary(block_dict)
		if not needed:
			total_removable += 1
	print(total_removable)


main()
