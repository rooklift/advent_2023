def hash(s):
	ret = 0
	for c in s:
		ret += ord(c)
		ret *= 17
		ret %= 256
	return ret

def main():
	with open("15_input.txt") as f:
		inp = f.read().strip()
	parts = inp.split(",")
	print(parts)
	total = 0
	for part in parts:
		total += hash(part)
	print(total)

main()
