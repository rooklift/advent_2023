def parse(filename):

	with open(filename) as f:
		lines = f.read().split("\n")
		lines.append("")				# Add empty line at end to ensure parse works.

	seeds = []		# What we are
	maps = []		# returning

	name = ""		# Our variables
	ints = []		# while parsing

	for line in lines:
		if line.strip() == "":			# Empty line signifies end of section.
			if name == "":
				pass
			elif name == "seeds":
				seeds = ints[::]
			else:
				maps.append(Map(name, ints))
			name = ""
			ints = []
			continue
		if ":" in line:
			name = line.split(":")[0]
			tokens = line.split(":")[1].split()
		else:
			tokens = line.split()
		ints += [int(token) for token in tokens]

	return seeds, maps

class Map:

	def __init__(self, name, ints):
		self.source = name.split("-")[0]				# We actually don't need this info, we can use the order
		self.dest = name.split("-")[-1].split()[0]		# in the list of maps, since the input file is in order
		self.ranges = []
		self.adjustments = []

		triples = zip(ints[0::3], ints[1::3], ints[2::3])

		for item in triples:
			dest = item[0]
			source = item[1]
			length = item[2]
			diff = dest - source
			self.ranges.append(range(source, source + length))
			self.adjustments.append(diff)

	def adjust(self, val):
		for i, r in enumerate(self.ranges):
			if val in r:
				return val + self.adjustments[i]
		return val

	def __repr__(self):
		return "{} to {} map".format(self.source, self.dest)

def main():
	seeds, maps = parse("05_input.txt")
	result = None
	for val in seeds:
		for m in maps:
			val = m.adjust(val)
		if result == None or val < result:
			result = val
	print(result)


main()
