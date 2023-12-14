def parse(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f.read().split("\n") if line.strip() != ""]
	ret = []
	for x in range(len(lines[0])):
		ret.append([])
	for y in range(len(lines)):
		for x, c in enumerate(lines[y]):
			ret[x].append(c)
	return ret

def main():
	arr = parse("14_input.txt")
	runs = []
	width, height = [len(arr), len(arr[0])]
	for x in range(width):
		hash_y = -1
		rocks = 0
		for y in range(height):
			if arr[x][y] == "O":
				rocks += 1
			elif arr[x][y] == "#":
				if rocks > 0:
					runs.append((hash_y + 1, rocks))		# Runs start at the first rock
					rocks = 0
				hash_y = y
		if rocks > 0:
			runs.append((hash_y + 1, rocks))
	total = 0
	for run in runs:
		total += ((height - run[0])) * run[1] - (run[1] * (run[1] - 1) / 2)
	print(int(total))

main()
