import pathlib

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-6-input-1.txt').read_text().strip()

def parse(puzzle_input):
	data = [x for x in puzzle_input]
	return data

def locateMarker(data):
    for x in range(len(data)-13):
        #print([[data[x+i],data[x+i+1:x+4]] for i in range(3)])
        if len([data[x+i] for i in range(14) if data[x+i] not in data[x+i+1:x+14]]) == 14:
            return [data[x+i] for i in range(14) if data[x+i] not in data[x+i+1:x+14]], x, data[x], data[x+14], x+14



print(locateMarker(parse(puzzle_input)))