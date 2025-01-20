from aocd import get_data
data = get_data(day=9, year=2024)
diskMap = []
id = -1
for i in range(len(data)):
    size = int(data[i])
    if i % 2 == 0:
        id += 1
        temp = [id] * size
        diskMap.extend(temp)

    else:
        temp = ["."] * size
        diskMap.extend(temp)

def moveFile(diskMap, spaceStart, spaceEnd, start, end):
    tempStart = start
    for i in range(spaceStart, spaceEnd + 1):
        diskMap[i], diskMap[tempStart] = diskMap[tempStart], diskMap[i]
        tempStart += 1

def findFreeEstateLocation(diskMap, targetLength, endIndex):
    start = end = 0
    currLength = 0
    while start != endIndex and end != endIndex:
        if diskMap[start] != ".":
            start += 1
            end += 1
        elif diskMap[start] == "." and diskMap[end] == ".":
            if currLength >= targetLength:
                return start, end - 1
            end += 1
            currLength += 1
        elif diskMap[start] == "." and diskMap[end] != ".":
            if currLength < targetLength:
                currLength = 0
                start = end = end
                continue
            else:
                return start, end - 1
    if end - start < targetLength:
        return -1, -1
    else:
        return start, end - 1

def findIDLocation(diskMap, id, lastUsed):
    start = end = lastUsed
    while end != 0 and start != 0:
        if diskMap[end] != id:
            end -= 1
            start -= 1
        elif diskMap[end] == id and diskMap[start] == id:
            start -= 1
        elif diskMap[end] == id and diskMap[start] != id:
            start += 1
            break
    return start, end


lastUsed = len(diskMap) - 1
for i in range(id, -1, -1):
    startIndex, endIndex = findIDLocation(diskMap, i, lastUsed)
    lastUsed = startIndex
    length = endIndex - startIndex + 1
    spaceStartIndex, spaceEndIndex = findFreeEstateLocation(diskMap, length, startIndex)
    if spaceStartIndex != -1 and spaceEndIndex != -1:
        moveFile(diskMap,spaceStartIndex,spaceEndIndex, startIndex, endIndex)


sum = 0
for index, value in enumerate(diskMap):
    if value == ".":
        continue
    sum += index * value

print(sum)
