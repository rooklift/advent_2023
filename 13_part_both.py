def parse(filename):
	with open(filename) as f:
		content = f.read()
	ret = []
	parts = content.split("\n\n")
	for part in parts:
		pattern = [line.strip() for line in part.split("\n") if line.strip() != ""]
		ret.append(pattern)
	return ret

def score(lines, desired_diff, horizontal = False):
	if not horizontal:
		vert_lines = []
		for x in range(len(lines[0])):
			vert_lines.append("".join([line[x] for line in lines]))
		lines = vert_lines
	for i in range(1, len(lines)):
		top = lines[:i]
		bottom = lines[i:]
		if symmetry_value(top, bottom) == desired_diff:
			return 100 * len(top) if horizontal else len(top)
	return 0

def symmetry_value(top, bottom):			# How far from being symmetric the lines are. 0 means perfectly symmetric, 1 means 1 flaw, etc.
	ret = 0
	ti = len(top) - 1
	bi = 0
	while ti >= 0 and bi < len(bottom):
		ret += line_diff(top[ti], bottom[bi])
		ti -= 1
		bi += 1
	return ret

def line_diff(line_a, line_b):
	ret = 0
	for i in range(len(line_a)):
		if line_a[i] != line_b[i]:
			ret += 1
	return ret

def main(desired_diff):
	patterns = parse("13_input.txt")
	total = 0
	for pattern in patterns:
		total += score(pattern, desired_diff, False)
		total += score(pattern, desired_diff, True)
	print(total)

main(0)
main(1)
