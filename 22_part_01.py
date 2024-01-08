def parse(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f.read().split("\n") if line.strip() != ""]
	ret = dict()
	for line in lines:
		params = [int(s) for s in line.replace("~", ",").split(",")]
		shape = Shape(*params)
		ret[shape.id] = shape
	return ret

class Shape:

	next_id = 0

	def __init__(self, x1, y1, z1, x2, y2, z2):		# We can assume x1 <= x2 etc...
		self.id = Shape.next_id
		Shape.next_id += 1
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

	def has_supporters(self, occupied_spots):

		# If vertical shape...

		if self.blocks[0][2] != self.blocks[-1][2]:
			test = (self.blocks[0][0], self.blocks[0][1], self.min_z() - 1)
			if test in occupied_spots:
				return True
			else:
				return False

		# Otherwise, this is a horizontal shape...

		for block in self.blocks:
			test = (block[0], block[1], block[2] - 1)
			if test in occupied_spots:
				return True
		return False

	def remove_from_dict(self, d):
		for block in self.blocks:
			del d[block]

	def add_to_dict(self, d):
		for block in self.blocks:
			d[block] = self.id

	def drop(self, occupied_spots):
		self.remove_from_dict(occupied_spots)
		self.blocks = [(o[0], o[1], o[2] - 1) for o in self.blocks]
		self.add_to_dict(occupied_spots)

	def has_exactly_one_supporter(self, occupied_spots):

		# If vertical shape...

		if self.blocks[0][2] != self.blocks[-1][2]:
			test = (self.blocks[0][0], self.blocks[0][1], self.min_z() - 1)
			if test in occupied_spots:
				return True
			else:
				return False

		# Otherwise, this is a horizontal shape...

		supporter_ids = set()

		for block in self.blocks:
			test = (block[0], block[1], block[2] - 1)
			if test in occupied_spots:
				supporter_ids.add(occupied_spots[test])

		return len(supporter_ids) == 1

	def is_necessary(self, shapes, occupied_spots):

		# Shape is necessary if:
		# 	It supports any shape
		#	No other shape supports that shape

		supported_shapes = set()

		# If vertical shape...

		if self.blocks[0][2] != self.blocks[-1][2]:

			test = (self.blocks[0][0], self.blocks[0][1], self.max_z() + 1)
			if test in occupied_spots:
				supported_shapes.add(shapes[occupied_spots[test]])

		else:		# Otherwise, this is a horizontal shape...

			for block in self.blocks:
				test = (block[0], block[1], block[2] + 1)
				if test in occupied_spots:
					supported_shapes.add(shapes[occupied_spots[test]])

		for shape in supported_shapes:
			if shape.has_exactly_one_supporter(occupied_spots):
				return True

		return False

def main():

	shapes = parse("22_input.txt")		# id --> shape

	occupied_spots = dict()				# (x,y,z) --> id
	for shape in shapes.values():
		for block in shape.blocks:
			occupied_spots[block] = shape.id

	while True:
		did_work = False
		for shape in shapes.values():
			while not (shape.has_supporters(occupied_spots) or shape.min_z() == 1):
				shape.drop(occupied_spots)
				did_work = True
		if not did_work:
			break

	total_removable = 0

	for sid, shape in shapes.items():
		needed = shape.is_necessary(shapes, occupied_spots)
		if not needed:
			total_removable += 1

	print(total_removable)


main()


