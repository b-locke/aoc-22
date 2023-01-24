import pathlib
import itertools
 
stacks = [[y for y in x] for x in ['','LNWTD', 'CPH', 'WPHNDGMJ', 'CWSNTQL', 'PHCN', 'THNDMWQB', 'MBRJGSL', 'ZNWGVBRT', 'WGDNPL']]

	  

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-5-input-1.txt').read_text().strip()


def parse(puzzle_input):
	data = [line.split(' ') for line in puzzle_input.splitlines()]
	return data

def moveCrates(data):
	for x in data:
		m = int(x[1])
		f = int(x[3])
		t = int(x[5])
		for y in range(m):
			stacks[t].append(stacks[f][-1])
			stacks[f].pop(-1)

moveCrates(parse(puzzle_input))

print(''.join([x[-1] for x in stacks[1:]]))
print(stacks)