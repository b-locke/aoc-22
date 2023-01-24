import pathlib

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-12-input-1.txt').read_text().strip()
alphaList = ['S', 'a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'E']

def parse(data):
	data = [[x for x in line] for line in data.splitlines()]
	return data

def hillClimbing(dataMap):
    start = [[[x, y] for y in range(len(dataMap[x])) if dataMap[x][y] == 'S'] for x in range(len(dataMap)) if 'S' in dataMap[x]][0][0]
    currentPosition = 'S'
    visitedList = [start]
    x = start[0]
    y = start[1]
    pathList = [[start]]
    count = 0

    while currentPosition != 'E' and count < 10000:
        count += 1
        pathListLengths = [len(x) for x in pathList]
        pathListMin = min(pathListLengths)
        indexOfMinPath = pathListLengths.index(pathListMin)
        currentPath = pathList[indexOfMinPath].copy()
        x = currentPath[-1][0]
        y = currentPath[-1][1]
        currentPosition = dataMap[x][y]
        if currentPosition == 'S':
            currentPosition = 'a'
        #print(pathList)

        if x != 0 and [x - 1, y] not in visitedList:
            up = dataMap[x - 1][y]
            if alphaList.index(up) - alphaList.index(currentPosition) <= 1:
                newPath = currentPath.copy()
                newPath.append([x - 1, y])
                pathList.append(newPath)
                visitedList.append([x - 1, y])

        if y != len(dataMap[0]) - 1 and [x, y + 1] not in visitedList:
            right = dataMap[x][y + 1]
            if alphaList.index(right) - alphaList.index(currentPosition) <= 1:
                newPath = currentPath.copy()
                newPath.append([x, y + 1])
                pathList.append(newPath)
                visitedList.append([x, y + 1])

        if x != len(dataMap) - 1 and [x + 1, y] not in visitedList:
            down = dataMap[x + 1][y]
            if alphaList.index(down) - alphaList.index(currentPosition) <= 1:
                newPath = currentPath.copy()
                newPath.append([x + 1, y])
                pathList.append(newPath)
                visitedList.append([x + 1, y])

        if y != 0 and [x, y - 1] not in visitedList:
            left = dataMap[x][y - 1]
            if alphaList.index(left) - alphaList.index(currentPosition) <= 1:
                newPath = currentPath.copy()
                newPath.append([x, y - 1])
                pathList.append(newPath)
                visitedList.append([x, y - 1])

        pathList.remove(currentPath)

        if currentPosition == 'E':
            return len(currentPath)

print(hillClimbing(parse(puzzle_input)))