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

	# The input is special and is designed to guarantee that each of the 6 trips
	# enters a perfect loop that always takes the same length of time. Thus, we
	# just need to find the length of each of the 6 loops then do some LCM stuff.

	loop_lengths = []

	for loc in locs:
		i = 0
		while True:
			c = directions[i % len(directions)]
			i += 1
			if c == "L":
				loc = m[loc][0]
			else:
				loc = m[loc][1]
			if loc.endswith("Z"):
				loop_lengths.append(i)
				break

	print(loop_lengths)		# Then send this to an online calculator (how do you LCM??)

main()
