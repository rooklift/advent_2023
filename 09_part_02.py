def parse(filename):
	with open(filename) as f:
		rawlines = [line.strip() for line in f.read().split("\n") if line.strip() != ""]
		return [[int(token) for token in line.split()] for line in rawlines]

def all_zeros(arr):
	for item in arr:
		if item != 0:
			return False
	return True

def next_subline(line):
	ret = []
	for n in range(1, len(line)):
		ret.append(line[n] - line[n - 1])
	return ret

def extrapolate(line):
	sublines = [line[::]]
	while True:
		if all_zeros(sublines[-1]):
			break
		sublines.append(next_subline(sublines[-1]))
	while True:
		ret = 0
		for i in range(len(sublines) - 2, -1, -1):
			ret = sublines[i][0] - ret
		return ret

def main():
	lines = parse("09_input.txt")
	result = 0
	for line in lines:
		result += extrapolate(line)
	print(result)

main()
