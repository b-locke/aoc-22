import pathlib

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-8-input-1.txt').read_text().strip()

def parse(data):
	data = [[tree for tree in line] for line in data.splitlines()]
	return data

def findVisible(data):
    above = [x for x in data[0]]
    left = [x[0] for x in data]
    below = [x for x in data[-1]]
    right = [x[-1] for x in data]
    visibleList = []

    for x in range(1, len(data) - 1 ):
        for y in range(1, len(data[0]) - 1):
            position = data[x][y]
            a = above[y]
            l = left[x]
            if position > a:
                above[y] = position
                visibleList.append([x, y])
            if position > l:
                left[x] = position
                visibleList.append([x, y])

    for x in range(len(data) - 2, 0, - 1):
        print(right)
        for y in range(len(data[0]) - 2, 0, - 1):
            position = data[x][y]
            b = below[y]
            r = right[x]
            if position > b:
                below[y] = position
                visibleList.append([x, y])
            if position > r:
                right[x] = position
                visibleList.append([x, y])

    outputList = []
    [outputList.append(x) for x in visibleList if x not in outputList]
    return len(data) * 4 - 4 + len(outputList)

def testBackCount():
    for x in range(99, 1, -1):
        for y in range(99, 1, -1):
            print(x, y)
           
testList = [1,2,3,4,5,6,]
#print(testList[:3], testList[3:])
print(findVisible(parse(puzzle_input)))