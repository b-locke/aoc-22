import pathlib

puzzle_input = pathlib.Path('/Users/benmelodics/Desktop/Personal/adventofcode/day-11-input-test.txt').read_text().strip()

def parse(data):
	data = [line.strip().split(':') for line in data.splitlines() if len(line) > 1]
	return data

def monkeyDictCreation(data):
    monkeyDict = {}
    currentMonkey = 0
    for x in data:
        #print(x)
        if x[0].split()[0] == 'Monkey':
            #print (x[0])
            monkeyDict[x[0].split()[1]] = {}
            currentMonkey = x[0].split()[1]
            monkeyDict[currentMonkey]['inspection'] = 0
        elif x[0]  == 'Starting items':
            monkeyDict[currentMonkey]['items'] = [int(x) for x in x[1].strip().split(',')]
        elif x[0]  == 'Operation':
            monkeyDict[currentMonkey]['operation'] = x[1].strip().split(' ')[-2:]
        elif x[0]  == 'Test':
            monkeyDict[currentMonkey]['test'] = int(x[1].split(' ')[-1])
        elif x[0]  == 'If true':
            monkeyDict[currentMonkey]['true'] = x[1].split(' ')[-1]
        elif x[0]  == 'If false':
            monkeyDict[currentMonkey]['false'] = x[1].split(' ')[-1]       
    return monkeyDict

def simulateSimians(monkeyData, rounds):

    modAll = 1
    for d in [monkeyData[m]['test'] for m in monkeyData]:
        modAll *= d
    
    print('mod: ', modAll)

    for round in range(rounds):
        for m in monkeyData:
            monkey = monkeyData[m]
            for item in monkey['items']:

                monkeyData[m]['inspection'] += 1
                worryLevel = item

                if monkey['operation'][0] == '*':
                    if monkey['operation'][1] == 'old':
                        worryLevel *= worryLevel
                    else:
                        worryLevel *= int(monkey['operation'][1])
                else:
                    if monkey['operation'][1] == 'old':
                        worryLevel += worryLevel
                    else:
                        worryLevel += int(monkey['operation'][1])

                worryLevel = worryLevel % modAll

                if worryLevel % monkey['test'] == 0:
                    monkeyData[monkey['true']]['items'].append(worryLevel)
                else:
                    monkeyData[monkey['false']]['items'].append(worryLevel)
                
            monkeyData[m]['items'] = []
                    
    return [monkeyData[x]['inspection'] for x in monkeyData]


data = parse(puzzle_input)
monkeyData = monkeyDictCreation(data)
print(simulateSimians(monkeyData, 10000))
