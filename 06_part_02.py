def parse(filename):
	with open(filename) as f:
		lines = f.readlines()
	time = int("".join(lines[0].split(":")[1].split()))
	distance = int("".join(lines[1].split(":")[1].split()))
	return time, distance

def main():

	# If the input was bigger we'd maybe want to binary search
	# for the first and last winning button-time.

	race_time, winning_distance = parse("06_input.txt")
	wins = 0
	for button_time in range(race_time + 1):
		speed = button_time
		distance = speed * (race_time - button_time)
		if distance > winning_distance:
			wins += 1
	print(wins)

main()
