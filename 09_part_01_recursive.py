# The recursive solution is cuter.

def parse(filename):
	with open(filename) as f:
		rawlines = [line.strip() for line in f.read().split("\n") if line.strip() != ""]
		return [[int(token) for token in line.split()] for line in rawlines]

def extrapolate(line):
	if all(n == 0 for n in line):
		return 0
	subline = [line[n + 1] - line[n] for n in range(len(line) - 1)]
	return line[-1] + extrapolate(subline)

def main():
	lines = parse("09_input.txt")
	result = 0
	for line in lines:
		result += extrapolate(line)
	print(result)

main()
