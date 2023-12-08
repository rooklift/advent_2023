def parse(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f.read().split("\n") if line.strip() != ""]
	directions = lines[0]
	m = dict()
	startloc = None
	for line in lines[1:]:
		line = line.replace("(", "")
		line = line.replace(")", "")
		key, rest = [item.strip() for item in line.split("=")]
		value = tuple(item.strip() for item in rest.split(","))
		m[key] = value
	return directions, m

def main():
	directions, m = parse("08_input.txt")
	locs = [item for item in m.keys() if item.endswith("A")]
	i = 0
	while True:
		c = directions[i % len(directions)]
		i += 1
		end = True
		for n, loc in enumerate(locs):
			if c == "L":
				next_node = m[loc][0]
			else:
				next_node = m[loc][1]
			if not next_node.endswith("Z"):
				end = False
			locs[n] = next_node
		if end:
			break
	print(i)

main()
