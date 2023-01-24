import pathlib

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-10-input-1.txt').read_text().strip()

def parse(data):
	data = [line.split(' ') for line in data.splitlines()]
	return data

def generateGrid(width, height):
    return [['.' for x in range(width)] for x in range(height)]

def cycles(data):
    grid = generateGrid(40, 6)
    cycleCount = 0
    row = 0
    spritePos = 1
    for x in range(len(data)):
        if data[x][0] == 'noop':
            cycleCount += 1
            if cycleCount - 1 in [spritePos - 1, spritePos, spritePos + 1]:
                grid[row][cycleCount - 1] = '#'
            if cycleCount in [40, 80, 120, 160, 200]:
                cycleCount = 0
                row += 1
        else:
            cycleCount += 1
            if cycleCount - 1 in [spritePos - 1, spritePos, spritePos + 1]:
                grid[row][cycleCount - 1] = '#'
            if cycleCount in [40, 80, 120, 160, 200]:
                cycleCount = 0
                row += 1

            cycleCount += 1
            if cycleCount - 1 in [spritePos - 1, spritePos, spritePos + 1]:
                grid[row][cycleCount - 1] = '#'
            if cycleCount in [40, 80, 120, 160, 200]:
                cycleCount = 0
                row += 1
            spritePos += int(data[x][1])
    return grid

data = cycles(parse(puzzle_input))
for x in data:
    print (''.join(x))