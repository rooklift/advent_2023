words_normal = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
words_reversed = [word[::-1] for word in words_normal]

def nice_lines(filename):
	with open(filename) as f:
		return [line.strip() for line in f.readlines() if line.strip() != ""]

def first_value(s, words):

	lowest_numeric_index = None
	first_digit = None

	for n, c in enumerate(s):
		if c.isdigit():
			lowest_numeric_index = n
			first_digit = int(c)
			break

	lowest_word_index = None
	first_word = None

	for word in words:
		if word in s:
			i = s.index(word)
			if lowest_word_index == None or i < lowest_word_index:
				lowest_word_index = i
				first_word = word

	if first_digit == None and first_word == None:
		raise(ValueError)

	if first_word == None or lowest_numeric_index < lowest_word_index:
		return first_digit

	if first_digit == None or lowest_word_index < lowest_numeric_index:
		return words.index(first_word)

	raise(ValueError)

def main():
	count = 0
	for line in nice_lines("input"):
		first = first_value(line, words_normal)
		last = first_value(line[::-1], words_reversed)
		count += int("{}{}".format(first, last))
	print(count)

main()
