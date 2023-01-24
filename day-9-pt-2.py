import pathlib

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-9-test-input-2.txt').read_text().strip()

def parse(data):
	data = [line for line in data.splitlines()]
	return data

def headPath(data):
    headPath = []
    hx = 0
    hy = 0
    tailPath = [[0,0]]
    tx = 0
    ty = 0
    for x in range(len(data)):
        direction = data[x].split(' ')[0]
        match data[x].split(' '):
            case ['L', d]:
                for x in range(int(d)):
                    headPath.append([hx - 1, hy])
                    hx -= 1
                    if hx - tx < - 1:
                        tx = hx + 1
                        ty = hy
                        tailPath.append([tx, ty, direction])

            case ['R', d]:
                for x in range(int(d)):
                    headPath.append([hx + 1, hy])
                    hx += 1
                    if hx - tx > 1:
                        tx = hx - 1
                        ty = hy
                        tailPath.append([tx, ty, direction])
            case ['U', d]:
                for y in range(int(d)):
                    headPath.append([hx, hy + 1])
                    hy += 1
                    if hy - ty > 1:
                        ty = hy - 1
                        tx = hx
                        tailPath.append([tx, ty, direction])
            case ['D', d]:
                for y in range(int(d)):
                    headPath.append([hx, hy - 1])
                    hy -= 1
                    if hy - ty < -1:
                        ty = hy + 1
                        tx = hx
                        tailPath.append([tx, ty, direction])
    twoPath = [[0,0]]
    for x in range(1,len(tailPath)):
        i = 0
        if tailPath[x][2] == 'L':
            if tailPath[x][0] - twoPath[i][0] < -1 or tailPath[x][1] - twoPath[i][1] > 1 or tailPath[x][1] - twoPath[i][1] < -1:
                twoPath.append([tailPath[x][0] + 1, tailPath[x][1]])
                i += 1
        elif tailPath[x][2] == 'R':
            if tailPath[x][0] - twoPath[i][0] > 1 or tailPath[x][1] - twoPath[i][1] > 1 or tailPath[x][1] - twoPath[i][1] < -1:
                twoPath.append([tailPath[x][0] - 1, tailPath[x][1]])
                i += 1
        elif tailPath[x][2] == 'U':
            if tailPath[x][1] - twoPath[i][1] > 1 or tailPath[x][0] - twoPath[i][0] < -1 or tailPath[x][0] - twoPath[i][0] > 1:
                twoPath.append([tailPath[x][0], tailPath[x][1] - 1])
                i += 1
        elif tailPath[x][2] == 'D':
            if tailPath[x][1] - twoPath[i][1] < -1 or tailPath[x][0] - twoPath[i][0] < -1 or tailPath[x][0] - twoPath[i][0] > 1:
                twoPath.append([tailPath[x][0], tailPath[x][1] + 1])
                i += 1

    returnPath = []
    [returnPath.append(x) for x in tailPath if x not in returnPath]
    return twoPath

print(headPath(parse(puzzle_input)))