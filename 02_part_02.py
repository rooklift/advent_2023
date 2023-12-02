def nice_lines(filename):
	with open(filename) as f:
		return [line.strip() for line in f.readlines() if line.strip() != ""]

def power(s):
	minimums = {"red": 0, "green": 0, "blue": 0}
	s = s.split(":")[1]
	s = s.replace(";", ",")
	items = s.split(",")
	for item in items:
		item = item.strip()
		num = int(item.split(" ")[0])
		colour = item.split(" ")[1]
		if minimums[colour] < num:
			minimums[colour] = num
	return minimums["red"] * minimums["green"] * minimums["blue"]

def main():
	count = 0
	for line in nice_lines("02_input.txt"):
		count += power(line)
	print(count)

main()
