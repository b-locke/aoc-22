import pathlib

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-7-input-1.txt').read_text().strip()

def parse(puzzle_input):
	data = [line for line in puzzle_input.splitlines()]
	return data

def createDictTree(data):
    dirDict = {'/': []}
    dir = '/'
    for x in data:
        if x[0] == 'dir':
            dirDict[dir].append(x[1])
        elif x[0] != '$':
            dirDict[dir].append(int(x[0]))
        elif x[1] == 'cd' and x[2] != '..':
            dir = x[2]
            dirDict[dir] = []
    return dirDict

def calcTreeSize(data, queue=['/']):

    values = data[queue[-1]]
    print(queue)
    for y in range(len(values)):
        if type(values[y]) == str:
            queue.append(values[y])
            calcTreeSize(data, queue)
        elif y == len(values) - 1:
            if len(queue) == 1:
                return data
            else:
                data[queue[-2]][data[queue[-2]].index(queue[-1])] = sum(data[queue[-1]])
                queue.pop()
                calcTreeSize(data, queue)


'''def traverseTree(data, queue=[0], path=['/']):
    dirSum = 0
    #print(path)
    for y in data:
        #print(y, dirSum)
        y = y.split(' ')
        if y[0].isnumeric():
            dirSum += int(y[0])
        elif y[0] == 'dir':
            queue.append(data.index(f'$ cd {y[1]}'))
            path.append(y[1])
            dirSum += traverseTree(data[queue[-1] + 1:], queue)
        elif y[1] == 'cd':
            if y[2] != '/':
                if dirSum <= 100000:
                    print(dirSum)
                queue.pop()
                path.pop()
                return dirSum
    return dirSum'''
options = []

def traverseTree(data, i = 0):
    dirSum = 0
    lowSum = 0
    index = i
    while index < len(data) - 1:
        index += 1
        line = data[index].split(' ')

        if line[0].isnumeric():
            dirSum += int(line[0])

        elif line[0] == 'x':
            return dirSum, index - 1

        elif line[1] == 'cd':
            if line[2] != '..' and line[2] != '/':

                s, traversal = traverseTree(data, index)
                index += traversal - index
                dirSum += s

            elif line[2] == '..':
                if dirSum > 4965705:
                    print(dirSum)
                    options.append(dirSum)
                return dirSum, index
    
                
    return dirSum



'''def traverseTree(data, queue=[0], dirSumList=[]):
    dirList = [[0]]
    index = 0
    for y in data:
        y = y.split(' ')
        if y[0].isnumeric():
            dirList[0].append(y)
        elif y[1] == 'cd':
            if y[2] == '..':
                index -= 1
            else:
                index += 1'''


print(traverseTree(parse(puzzle_input)))
print(min(options))

'''def findSum(data):
    dataSum = []
    for x in data:
        x = x.split(' ')
        if x[1] =='cd':
            dataSum.append(x[2])
    return dataSum'''
#print(findSum(parse(puzzle_input)))


