import pathlib

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-8-input-1.txt').read_text().strip()

def parse(data):
	data = [[tree for tree in line] for line in data.splitlines()]
	return data

def scenicScore(data):
    highScore = 0
    for x in range(len(data)):
        for y in range(len(data[0])):
            left = 0
            right = 0
            up = 0
            down = 0
            if x != 0:
                for i in range(x - 1, -1, -1):
                    up += 1
                    if data[i][y] >= data[x][y] or i == - 1:
                        print(x, y, up)
                        break
            if x != 98:
                for i in range(x + 1, len(data)):
                    down += 1
                    if data[i][y] >= data[x][y] or i == len(data) - 1:
                        print(x, y, down)
                        break
            if y != 0:
                for i in range(y - 1, -1, -1):
                    left += 1
                    if data[x][i] >= data[x][y] or i == - 1:
                        print(x, y, left)
                        break
            if y != 98:
                for i in range(y + 1, len(data)):
                    right += 1
                    if data[x][i] >= data[x][y] or i == len(data) - 1:
                        print(x, y, right)
                        break

            if left * right * up * down > highScore:
                highScore = left * right * up * down

    return(highScore)
            
print(scenicScore(parse(puzzle_input)))

print([x for x in range(1 - 1,-1,-1)])
#print([x for x in range(0, len(parse(puzzle_input)))])


