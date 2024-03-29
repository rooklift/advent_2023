def parse(filename):
	with open(filename) as f:
		data = f.read()
	parts = [part for part in data.split("\n\n") if part.strip() != ""]
	seeds = make_seed_ranges([int(token) for token in parts[0].split(":")[1].split()])
	maps = []
	for part in parts[1:]:
		tokens = part.split(":")[1].split()
		ints = [int(token) for token in tokens]
		maps.append(Map(ints))
	return seeds, maps

def make_seed_ranges(ints):
	ranges = []
	for start, length in zip(ints[0::2], ints[1::2]):
		ranges.append(range(start, start + length))
	return ranges

class Map:
	def __init__(self, ints):
		self.ranges = []
		self.adjustments = []
		for dest, source, length in zip(ints[0::3], ints[1::3], ints[2::3]):
			diff = dest - source
			self.ranges.append(range(source, source + length))
			self.adjustments.append(diff)

	def adjust(self, n):
		for i, r in enumerate(self.ranges):
			if n in r:
				return n + self.adjustments[i]
		return n

	def needs_adjusting(self, n):						# True iff we have a range that includes n
		for r in self.ranges:
			if n in r:
				return True
		return False

	def last_n_outside_range(self, n):					# For some n that is not in a range, find the final number not in a range
		ret = None
		for r in self.ranges:
			if r[0] > n:
				if ret == None or r[0] < ret:
					ret = r[0] - 1
		return ret

	def last_n_inside_range(self, n):					# For some n that is in a range, find the final number in the range
		for r in self.ranges:
			if n in r:
				return r[-1]
		raise AssertionError							# This should be impossible

	def new_ranges(self, old_range):					# Given a single input range, return all output ranges
		ret = []
		n = old_range[0]
		while True:
			if n not in old_range:
				break
			if self.needs_adjusting(n):
				last_n_inside_range = self.last_n_inside_range(n)
				if old_range[-1] <= last_n_inside_range:
					end_of_new_range = self.adjust(old_range[-1])
				else:
					end_of_new_range = self.adjust(last_n_inside_range)
				ret.append(range(self.adjust(n), end_of_new_range + 1))
				n = last_n_inside_range + 1
			else:
				last_n_outside_range = self.last_n_outside_range(n)
				if last_n_outside_range == None:
					last_n_outside_range = old_range[-1]
				if old_range[-1] <= last_n_outside_range:
					end_of_new_range = self.adjust(old_range[-1])
				else:
					end_of_new_range = self.adjust(last_n_outside_range)
				ret.append(range(self.adjust(n), end_of_new_range + 1))
				n = last_n_outside_range + 1
		return ret

def main():
	ranges, maps = parse("05_input.txt")
	for m in maps:
		new_ranges = []
		for r in ranges:
			new_ranges += m.new_ranges(r)
		ranges = new_ranges
	print(min([r[0] for r in ranges]))

main()
