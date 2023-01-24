import pathlib
import itertools

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-3-input-1.txt').read_text().strip()


def parse(puzzle_input):
	data = [[line[:int(len(line)/2)],line[int(len(line)/2):]] for line in puzzle_input.splitlines()]
	return data

def difference(data):
    return [[y for y in x[0] if y in x[1]][0] for x in data]

def lowercase(data):
    return[ord(x) - 96 for x in data if x == x.lower()]

def uppercase(data):
    return[ord(x) - 38 for x in data if x == x.upper()]

data = difference(parse(puzzle_input))

data = lowercase(data) + uppercase(data)

print(sum(data))