import pathlib

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-7-input-1.txt').read_text().strip()

def parse(puzzle_input):
	data = [line for line in puzzle_input.splitlines()]
	return data

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
                if dirSum < 100000:
                    print(dirSum)
                    options.append(dirSum)
                return dirSum, index
    
                
    return dirSum


print(traverseTree(parse(puzzle_input)))
print(sum(options))

#print(findSum(parse(puzzle_input)))


