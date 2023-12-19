def parse(filename):
	with open(filename) as f:
		data = f.read()
	a, b = data.split("\n\n")
	a_lines = a.split()
	b_lines = b.split()
	workflows = []
	parts = []
	for line in a_lines:
		workflows.append(Workflow(line))
	for line in b_lines:
		parts.append(Part(line))
	return workflows, parts

class Workflow:

	def __init__(self, line):
		line = line[:-1]
		self.name, instructions = line.split("{")
		self.instructions = instructions.split(",")

	def process(self, part):
		for ins in self.instructions:
			if ":" not in ins:
				return ins
			test, dest = ins.split(":")
			key = test[0]
			val = int(test[2:])
			if test[1] == "<" and part[key] < val:
				return dest
			elif test[1] == ">" and part[key] > val:
				return dest

class Part:

	def __init__(self, line):
		self._d = dict()
		foo = line[1:-1].split(",")
		for item in foo:
			key, val = item.split("=")
			self[key] = int(val)

	def __getitem__(self, key):
		return self._d[key]

	def __setitem__(self, key, val):
		self._d[key] = val

def main():

	workflows, parts = parse("19_input.txt")
	wd = dict()
	for workflow in workflows:
		wd[workflow.name] = workflow

	result = 0

	for part in parts:
		dest = "in"
		while dest not in ["A", "R"]:
			workflow = wd[dest]
			dest = workflow.process(part)
		if dest == "A":
			result += part["x"] + part["m"] + part["a"] + part["s"]

	print(result)

main()
