def nice_lines(filename):
	with open(filename) as f:
		return [line.strip() for line in f.readlines() if line.strip() != ""]

def first_value(s):
	for c in s:
		if c.isdigit():
			return int(c)
	raise(ValueError)

def main():
	count = 0
	for line in nice_lines("input"):
		first = first_value(line)
		last = first_value(line[::-1])
		count += int("{}{}".format(first, last))
	print(count)

main()
