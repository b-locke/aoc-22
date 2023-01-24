import pathlib
import itertools

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-4-input-1.txt').read_text().strip()


def parse(puzzle_input):
	data = [[[int(x.split('-')[0]), int(x.split('-')[1])] for x in line.split(',')] for line in puzzle_input.splitlines()]
	return data

def evalContain(data):
	return len([x for x in data if x[0][0] >= x[1][0] and x[0][1] <= x[1][1] or x[0][0] <= x[1][0] and x[0][1] >= x[1][1]])

data = parse(puzzle_input)

print(evalContain(data))