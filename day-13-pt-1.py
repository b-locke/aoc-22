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
    orderedPairs = []
    unorderedPairs = []
    pairCount = 0
    for x in range(0, len(data), 2):
        pairCount += 1
        left = data[x]
        right = data[x+1]
        for y in range(max([len(left), len(right)]) - 1):
            if y > len(left) - 1 or y > len(right) - 1:
                break

            elif left[y] == '[' and right[y] == '[':
                continue

            elif left[y] == ']' and right[y] == '[':
                orderedPairs.append(pairCount)
                print('Left side is shorter', left[y], right[y])
                break
            
            elif left[y] == '[' and right[y] == ']':
                unorderedPairs.append(pairCount)
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
                orderedPairs.append(pairCount)
                print('Left side is shorter', left[y], right[y])
                break

            elif right[y] == ']':
                unorderedPairs.append(pairCount)
                print('Right side is shorter', left[y], right[y])
                break

            elif left[y] == '*' and right[y] == '*':
                continue

            elif left[y] == '*':
                unorderedPairs.append(pairCount)
                print('Right side is lower', left[y], right[y])
                break

            elif right[y] == '*':
                orderedPairs.append(pairCount)
                print('Left side is lower', left[y], right[y])
                break

            elif int(left[y]) < int(right[y]):
                orderedPairs.append(pairCount)
                print('Left side is lower', left[y], right[y])
                break
            
            elif int(left[y]) > int(right[y]):
                unorderedPairs.append(pairCount)
                print('Right side is lower', left[y], right[y])
                break

        print(left, right)

    return sum([x for x in orderedPairs])

print(compareLeftToRight(parse(puzzle_input)))