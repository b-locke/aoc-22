import pathlib

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-1-input-1.txt').read_text().strip()

def parse(puzzle_input):
	data = [sum([int(y) for y in x.split(',')]) for x in ','.join([line for line in puzzle_input.splitlines()]).split(',,')]
	return data

print(max(parse(puzzle_input)))
