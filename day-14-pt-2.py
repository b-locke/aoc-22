import pathlib

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-14-input-1.txt').read_text().strip()

def parse(data):
	data = [[[int(x) for x in x.strip().split(',')] for x in line.split('->')] for line in data.splitlines()]
	return data

def width(data):
    return max([max([data[x][y][0] for y in range(len(data[x]))]) for x in range(len(data))]) + min([min([data[x][y][0] for y in range(len(data[x]))]) for x in range(len(data))])

def height(data):
    return max([max([data[x][y][1] for y in range(len(data[x]))]) for x in range(len(data))])

def createCave(width, height):
	return [['.' for x in range(width)] for y in range(height)]

def convertCoordinates(data):
	return [[[data[x][y][0] - min([min([data[x][y][0] for y in range(len(data[x]))]) for x in range(len(data))]), data[x][y][1]] for y in range(len(data[x]))] for x in range(len(data))]

def fillCoordinates(data):
	completeList = []
	for x in range(len(data)):
		formationList = []
		for y in range(len(data[x]) - 1):
			if data[x][y][1] < data[x][y + 1][1]:
				formationList += [[data[x][y][0], data[x][y][1] + i] for i in range(data[x][y + 1][1] - data[x][y][1] + 1)]
			elif data[x][y][1] > data[x][y + 1][1]:
				formationList += [[data[x][y][0], data[x][y][1] - i] for i in range(data[x][y][1] + 1 - data[x][y + 1][1])]
			elif data[x][y][0] < data[x][y + 1][0]:
				formationList += [[data[x][y][0] + i, data[x][y][1]] for i in range(data[x][y + 1][0] - data[x][y][0] + 1)]
			elif data[x][y][0] > data[x][y + 1][0]:
				formationList += [[data[x][y][0] - i, data[x][y][1]] for i in range(data[x][y][0] + 1 - data[x][y + 1][0])]
		completeList.append(formationList)
	return completeList

def addCaveDetails(caveData, rockDetails, source):
	caveCopy = caveData.copy()
	for x in range(len(rockDetails)):
		for y in range(len(rockDetails[x])):
			caveCopy[rockDetails[x][y][1]][rockDetails[x][y][0]] = '#'
	caveCopy[source[1]][source[0]] = '+'
	return caveCopy

def addFloor(data):
    caveCopy = data.copy()
    caveCopy.append(['#' for x in range(len(caveCopy[0]))])
    return caveCopy

def modelingSand(caveData, unitsOfSand, source):
	caveCopy = caveData.copy()
	grainCount = 0
	for grain in range(unitsOfSand):
		sandState = 'falling'
		grainCount += 1
		sandy = source[1]
		sandx = source[0]
		while sandState == 'falling':
			if caveCopy[sandy + 1][sandx] == '.':
				sandy += 1
			elif caveCopy[sandy + 1][sandx - 1] == '.':
				sandx -= 1
				sandy += 1
			elif caveCopy[sandy + 1][sandx + 1] == '.':
				sandx += 1
				sandy += 1
			elif sandx == 500 and sandy == 0:
				return caveCopy, grainCount
			else:
				caveCopy[sandy][sandx] = 'o'
				sandState = 'rest'
	return caveCopy, grainCount

data = parse(puzzle_input)
width = width(data)
height = height(data) + 2
cave = createCave(width, height)
source = [500, 0]
detailedCave = addCaveDetails(addFloor(cave), fillCoordinates(data), source)
sandModeledCave, grainCount = modelingSand(detailedCave, 100000, source)

print(grainCount)

#for x in range(len(sandModeledCave[0])):
#	print(''.join(sandModeledCave[0][x]))

for x in range(len(detailedCave)):
	print(''.join(detailedCave[x]))
