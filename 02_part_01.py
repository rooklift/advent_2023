limits = {"red": 12, "green": 13, "blue": 14}

def nice_lines(filename):
	with open(filename) as f:
		return [line.strip() for line in f.readlines() if line.strip() != ""]

def check(s):
	s = s.split(":")[1]
	s = s.replace(";", ",")
	items = s.split(",")
	for item in items:
		item = item.strip()
		num = int(item.split(" ")[0])
		colour = item.split(" ")[1]
		if limits[colour] < num:
			return False
	return True

def game_number(s):
	return int(s.split(":")[0].split(" ")[1])

def main():
	count = 0
	for line in nice_lines("02_input.txt"):
		if check(line):
			count += game_number(line)
	print(count)

main()
