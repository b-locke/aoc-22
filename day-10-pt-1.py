import pathlib

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-10-input-1.txt').read_text().strip()

def parse(data):
	data = [line.split(' ') for line in data.splitlines()]
	return data

def checkCycle(cycleCount, signal, checkArray):
    if cycleCount in checkArray:
        print(signal * cycleCount, signal, cycleCount)
        return signal * cycleCount
    else:
        return 0 

def cycles(data):
    cycleCount = 0
    signal = 1
    sumSignal = 0
    for x in range(len(data)):
        if data[x][0] == 'noop':
            cycleCount += 1
            sumSignal += checkCycle(cycleCount, signal, [20, 60, 100, 140, 180, 220])
        else:
            cycleCount += 1
            sumSignal += checkCycle(cycleCount, signal, [20, 60, 100, 140, 180, 220])
            cycleCount += 1
            sumSignal += checkCycle(cycleCount, signal, [20, 60, 100, 140, 180, 220])
            signal += int(data[x][1])
    return sumSignal

print(cycles(parse(puzzle_input)))