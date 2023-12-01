words_normal = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
words_reversed = [word[::-1] for word in words_normal]

def nice_lines(filename):
	with open(filename) as f:
		return [line.strip() for line in f.readlines() if line.strip() != ""]

def first_value(s, words):
	lowest_index = None
	ret = None
	for n, c in enumerate(s):
		if c.isdigit():
			lowest_index = n
			ret = int(c)
			break
	for word in words:
		if word in s:
			i = s.index(word)
			if lowest_index == None or i < lowest_index:
				lowest_index = i
				ret = words.index(word)
	if ret == None:
		raise(ValueError)
	return ret

def main():
	count = 0
	for line in nice_lines("01_input.txt"):
		first = first_value(line, words_normal)
		last = first_value(line[::-1], words_reversed)
		count += int("{}{}".format(first, last))
	print(count)

main()
