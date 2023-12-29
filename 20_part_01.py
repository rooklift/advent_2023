def parse(filename):

	with open(filename) as f:
		lines = [line for line in f.read().split("\n") if line.strip() != ""]

	nodes = []
	for line in lines:
		tag, rest = line.split(" -> ")
		rest = rest.split(", ")
		nodes.append(Node(tag, rest))

	d = dict()
	for node in nodes:
		d[node.name] = node

	# Populate the node outputs with actual objects:

	for node in nodes:
		for s in node.output_strings:
			if s not in d:
				d[s] = Node("%" + s, [])
				print("Added " + s)
			node.outputs.append(d[s])

	# Populate the node outputs with actual objects:

	for node in nodes:
		for output in node.outputs:
			assert(node not in output.inputs)
			output.inputs.append(node)

	return d

class Node:

	def __init__(self, tag, dests):
		self.type = tag[0]
		self.name = tag[1:] if tag != "broadcaster" else "broadcaster"
		self.inputs = []
		self.outputs = []
		self.output_strings = dests[::]
		self.ff_on = False
		self.conj_highs = set()

	def receive(self, source, input_high):

		if input_high:
			self.conj_highs.add(source.name)
		else:
			self.conj_highs.discard(source.name)
			self.ff_on = not self.ff_on

		output_high = False

		if self.type == "%":
			if input_high:
				return []					# i.e. sends no pulse
			else:
				output_high = self.ff_on

		if self.type == "&":
			output_high = len(self.conj_highs) != len(self.inputs)

		return [(self, dest, output_high) for dest in self.outputs]


def main():
	world = parse("20_input.txt")
	low, high = 0, 0
	for n in range(1000):
		l, h = pulse(world)
		low += l
		high += h
	print("Part 1:", low * high)

def pulse(world):

	low, high = 1, 0

	todo = []		# Source, dest, high?

	for dest in world["broadcaster"].outputs:
		todo.append((world["broadcaster"], dest, False))

	while len(todo) > 0:
		item = todo.pop(0)
		if item[2]:
			high += 1
		else:
			low += 1
		todo += item[1].receive(item[0], item[2])

	return low, high


main()