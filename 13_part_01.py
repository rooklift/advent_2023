def parse(filename):
	with open(filename) as f:
		content = f.read()
	ret = []
	parts = content.split("\n\n")
	for part in parts:
		pattern = [line.strip() for line in part.split("\n") if line.strip() != ""]
		ret.append(pattern)
	return ret

def score(lines, horizontal = False):

	if not horizontal:
		vert_lines = []
		for x in range(len(lines[0])):
			vert_lines.append("".join([line[x] for line in lines]))
		lines = vert_lines

	for i in range(1, len(lines)):
		top = lines[:i]
		bottom = lines[i:]
		if symmetric(top, bottom):
			return 100 * len(top) if horizontal else len(top)

	return 0

def symmetric(top, bottom):
	ti = len(top) - 1
	bi = 0
	while ti >= 0 and bi < len(bottom):
		if top[ti] != bottom[bi]:
			return False
		ti -= 1
		bi += 1
	return True

def main():
	patterns = parse("13_input.txt")
	total = 0
	for pattern in patterns:
		total += score(pattern, False)
		total += score(pattern, True)
	print(total)

main()
