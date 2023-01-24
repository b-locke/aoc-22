import pathlib
import re

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-15-input-test.txt').read_text().strip()

def parse(data):
	data = [line for line in data.splitlines()]
	return data

def findSensorPositions(data):
    positionsList = []
    for line in data:
        splitLine = re.split(',|\:', line)
        positions = []
        for i in splitLine:
            match i.split('='):
                case ['Sensor at x', position]:
                    positions.append(int(position))
                case [' y', position]:
                    positions.append(int(position))
                case [' closest beacon is at x', position]:
                    positions.append(int(position))
                case [' y', position]:
                    positions.append(int(position))
        positionsList.append(positions)
    return positionsList

def createMap(data):
    minSensorx = min([x[0] for x in data])
    maxSensorx = max([x[0] for x in data])
    minSensory = min([x[1] for x in data])
    maxSensory = max([x[1] for x in data])
    minBeaconx = min([x[2] for x in data])
    maxBeaconx = max([x[2] for x in data])
    minBeacony = min([x[3] for x in data])
    maxBeacony = max([x[3] for x in data])

    minx = min(minSensorx, minBeaconx)
    maxx = max(maxSensorx, maxBeaconx)
    miny = min(minSensory, minBeacony)
    maxy = max(maxSensory, maxBeacony)

    grid = [['.' for x in range(minx, maxx)] for y in range(miny, maxy)]

    for line in data:
        grid[line[0]][line[1]] = 'S'
        grid[line[2]][line[3]] = 'B'
        
    return grid


data = findSensorPositions(parse(puzzle_input))
grid = createMap(data)
for x in grid:
    print(''.join(x))