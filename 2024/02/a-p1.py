from aocd import get_data
data = get_data(day=2, year=2024)
dataByLines = data.splitlines()

def isIncreasing(data):
    for index in range(1, len(data)):
        if int(data[index - 1]) < int(data[index]):
            continue
        else:
            return False
    return True

def isDecreasing(data):
    for index in range(1, len(data)):
        if int(data[index - 1]) > int(data[index]):
            continue
        else:
            return False
    return True

def isIncrementSafe(data):
    for index in range(1, len(data)):
        if abs(int(data[index - 1]) - int(data[index])) >= 1 and abs(int(data[index - 1]) - int(data[index])) <= 3:
            continue
        else:
            return False
    return True

dataList = []
for data in dataByLines:
    dataList.append(data.split())

count = 0


for data in dataList:
    if not isIncreasing(data) and not isDecreasing(data):
        continue
    if not isIncrementSafe(data):
        continue
    count += 1

print(count)
