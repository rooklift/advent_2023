def parse(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f.read().split("\n") if line.strip() != ""]
	ret = []
	for line in lines:
		string, rest = line.split(" ")
		nums = [int(s) for s in rest.split(",")]
		ret.append(Item(string, nums))
	return ret

class Item:
	def __init__(self, string, nums):
		self.state = list(string)
		self.nums = nums

	def unknowns(self):
		return self.state.count("?")

	def hashes(self):
		return self.state.count("#")

	def needed_hashes(self):					# How many ? must be converted to #
		return sum(self.nums) - self.hashes()

	def valid_combos(self):
		ret = 0
		need = self.needed_hashes()
		for i in range((2 ** self.unknowns())):
			if i.bit_count() == need:
				if self.is_valid_combo(i):
					ret += 1
		return ret

	def is_valid_combo(self, i):
		unknowns = self.unknowns()
		s = bin(i)[2:]							# Remove "0b" prefix
		s = ("0" * (unknowns - len(s))) + s		# Make string length equal the number of unknowns
		fixed_list = self.state[::]
		s_index = 0
		l_index = 0
		while l_index < len(fixed_list):
			if fixed_list[l_index] == "?":
				fixed_list[l_index] = "#" if s[s_index] == "1" else "."
				s_index += 1
				l_index += 1
			else:
				l_index += 1
		return self.fixed_list_matches_nums(fixed_list)

	def fixed_list_matches_nums(self, fixed_list):
		nums = []
		acc = 0
		for c in fixed_list:
			if c == "#":
				acc += 1
			else:
				if acc > 0:
					nums.append(acc)
					acc = 0
		if acc > 0:
			nums.append(acc)
		return nums == self.nums

def main():
	items = parse("12_input.txt")

	total = 0

	for i, item in enumerate(items):
		combos = item.valid_combos()
		total += combos
		print(i, combos)

	print(total)

main()
