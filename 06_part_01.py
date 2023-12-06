def parse(filename):
	with open(filename) as f:
		lines = f.readlines()
	times = [int(s) for s in lines[0].split(":")[1].split()]
	distances = [int(s) for s in lines[1].split(":")[1].split()]
	return list(zip(times, distances))

def main():
	mult = 1

	tuples = parse("06_input.txt")

	for race_time, winning_distance in tuples:
		wins = 0
		for button_time in range(race_time + 1):
			speed = button_time
			distance = speed * (race_time - button_time)
			if distance > winning_distance:
				wins += 1
		mult *= wins

	print(mult)

main()
