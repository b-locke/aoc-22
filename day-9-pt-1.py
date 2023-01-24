import pathlib

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-9-input-1.txt').read_text().strip()

def parse(data):
	data = [line for line in data.splitlines()]
	return data

def headPath(data):
    headPath = []
    hx = 0
    hy = 0
    tailPath = [[0,0]]
    tailMoves = []
    tx = 0
    ty = 0
    for x in range(len(data)):
        match data[x].split(' '):
            case ['L', d]:
                for x in range(int(d)):
                    headPath.append([hx - 1, hy])
                    hx -= 1
                    if hx - tx < - 1:
                        tx = hx + 1
                        ty = hy
                        tailPath.append([tx, ty])

            case ['R', d]:
                for x in range(int(d)):
                    headPath.append([hx + 1, hy])
                    hx += 1
                    if hx - tx > 1:
                        tx = hx - 1
                        ty = hy
                        tailPath.append([tx, ty])
            case ['U', d]:
                for y in range(int(d)):
                    headPath.append([hx, hy + 1])
                    hy += 1
                    if hy - ty > 1:
                        ty = hy - 1
                        tx = hx
                        tailPath.append([tx, ty])
            case ['D', d]:
                for y in range(int(d)):
                    headPath.append([hx, hy - 1])
                    hy -= 1
                    if hy - ty < -1:
                        ty = hy + 1
                        tx = hx
                        tailPath.append([tx, ty])
    returnPath = []
    [returnPath.append(x) for x in tailPath if x not in returnPath]
    return len(returnPath)

print(headPath(parse(puzzle_input)))