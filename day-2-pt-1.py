import pathlib

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-2-input-1.txt').read_text().strip()
scores = {'A X': 4, 'A Y': 8, 'A Z': 3,
          'B X': 1, 'B Y': 5, 'B Z': 9,
          'C X': 7, 'C Y': 2, 'C Z': 6}

def parse(puzzle_input):
	data = [line for line in puzzle_input.splitlines()]
	return data

data = parse(puzzle_input)
totalScore = 0

for x in data:
    totalScore += scores[x]



print(totalScore)