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

	def has_supporters(self, block_id_dict):
		for spot in self.spots_below():
			if spot in block_id_dict:
				return True
		return False

	def remove_from_dict(self, d):
		for block in self.blocks:
			del d[block]

	def add_to_dict(self, d):
		for block in self.blocks:
			d[block] = self.id

	def drop(self, block_id_dict):
		self.remove_from_dict(block_id_dict)
		self.blocks = [(o[0], o[1], o[2] - 1) for o in self.blocks]
		self.add_to_dict(block_id_dict)

	def hide(self, id_shape_dict, block_id_dict):
		self.remove_from_dict(block_id_dict)
		del id_shape_dict[self.id]

def main():
	id_shape_dict = parse("22_input.txt")		# id --> shape
	block_id_dict = dict()						# (x,y,z) --> id
	for shape in id_shape_dict.values():
		for block in shape.blocks:
			block_id_dict[block] = shape.id
	while True:
		did_work = False
		for shape in id_shape_dict.values():
			while not (shape.has_supporters(block_id_dict) or shape.min_z() == 1):
				shape.drop(block_id_dict)
				did_work = True
		if not did_work:
			break
	total = 0
	for shape in id_shape_dict.values():
		total += count_dependencies(shape, id_shape_dict, block_id_dict)
	print(total)

def count_dependencies(shape, id_shape_dict, block_id_dict):
	id_shape_dict = id_shape_dict.copy()
	block_id_dict = block_id_dict.copy()
	shape.hide(id_shape_dict, block_id_dict)
	ret = 0
	while True:
		did_work = False
		for shape in list(id_shape_dict.values()):
			if not (shape.has_supporters(block_id_dict) or shape.min_z() == 1):
				shape.hide(id_shape_dict, block_id_dict)
				ret += 1
				did_work = True
		if not did_work:
			break
	return ret


main()
