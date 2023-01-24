import pathlib
from ast import literal_eval

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-13-input-1.txt').read_text().strip()

def parse(data):
	data = [[x for x in line if x != ','] for line in data.splitlines() if len(line) > 0]
	return data

def literalParse(data):
	data = [literal_eval(line) for line in data.splitlines() if len(line) > 0]
	return data

def compareLeftToRight(data):

    orderedList = [data[0]]

    for x in range(1, len(data)):
        z = 0

        while z < len(orderedList):
            left = data[x].copy()
            right = orderedList[z].copy()

            if left in orderedList:
                break

            for y in range(max([len(left), len(right)]) - 1):

                if y > len(left) - 1 or y > len(right) - 1:
                    break

                elif left[y] == '[' and right[y] == '[':
                    continue

                elif left[y] == ']' and right[y] == '[':
                    orderedList.insert(z, data[x])
                    z += 1
                    print('Left side is shorter', left[y], right[y])
                    break
                
                elif left[y] == '[' and right[y] == ']':
                    print('Right side is shorter', left[y], right[y])
                    break

                elif left[y] == '[':
                    newList = right[y]
                    right.pop(y)
                    right.insert(y, '[')
                    right.insert(y + 1, newList)
                    right.insert(y + 2, ']')

                elif right[y] == '[':
                    newList = left[y]
                    left.pop(y)
                    left.insert(y, '[')
                    left.insert(y + 1, newList)
                    left.insert(y + 2, ']')

                elif left[y] == ']' and right[y] == ']':
                    continue

                elif left[y] == ']':
                    orderedList.insert(z, data[x])
                    z += 1
                    print('Left side is shorter', left[y], right[y])
                    break

                elif right[y] == ']':
                    print('Right side is shorter', left[y], right[y])
                    break

                elif left[y] == '*' and right[y] == '*':
                    continue

                elif left[y] == '*':
                    print('Right side is lower', left[y], right[y])
                    break

                elif right[y] == '*':
                    orderedList.insert(z, data[x])
                    z += 1
                    print('Left side is lower', left[y], right[y])
                    break

                elif int(left[y]) < int(right[y]):
                    orderedList.insert(z, data[x])
                    z += 1
                    print('Left side is lower', left[y], right[y])
                    break
                
                elif int(left[y]) > int(right[y]):
                    print('Right side is lower', left[y], right[y])
                    break

            z += 1

        if left not in orderedList:
            print('left added to end')
            orderedList.append(data[x])

    return orderedList

data = compareLeftToRight(parse(puzzle_input))
for x in data:
    print(x)

twoIndex = (data.index(['[', '[', '2', ']', ']']) + 1)
sixIndex = (data.index(['[', '[', '6', ']', ']']))
print(twoIndex * sixIndex, twoIndex, sixIndex)