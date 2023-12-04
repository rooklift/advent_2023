def nice_lines(filename):
	with open(filename) as f:
		return [line.strip() for line in f.readlines() if line.strip() != ""]

def main():
	lines = nice_lines("04_input.txt")
	result = 0
	for line in lines:
		tokens1 = line.split(":")[1].split("|")[0].split()
		tokens2 = line.split(":")[1].split("|")[1].split()
		set1 = set(tokens1)
		set2 = set(tokens2)
		intersection = set1.intersection(set2)
		if len(intersection) > 0:
			result += 2 ** (len(intersection) - 1)
	print(result)

main()
