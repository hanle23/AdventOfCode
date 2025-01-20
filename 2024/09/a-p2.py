from aocd import get_data
data = get_data(day=9, year=2024)
# data = "2333133121414131402"
diskMap = []
id = 0
for i in range(len(data)):
    size = int(data[i])
    if i % 2 == 0:
        temp = [id] * size
        diskMap.extend(temp)
        id += 1
    else:
        temp = ["."] * size
        diskMap.extend(temp)
result = ""
start, end = 0, len(diskMap) - 1
while diskMap[end] == "." and end != start:
    end -= 1
def moveFile(diskMap, startIndex, endIndex):
    length = endIndex - startIndex + 1
    targetStartIndex = -1
    targetEndIndex = -1
    for i in range(startIndex):
        if diskMap[i] == "." and targetStartIndex == -1:
            targetStartIndex = i
            targetEndIndex = i
        elif diskMap[i] == "." and targetStartIndex != -1:
            targetEndIndex = i
        elif diskMap[i] != "." and targetStartIndex != -1:
            targetLength = targetEndIndex - targetStartIndex + 1
            if targetLength >= length:
                for j in range(startIndex, endIndex + 1):
                    diskMap[j], diskMap[targetStartIndex] = diskMap[targetStartIndex], diskMap[j]
                    targetStartIndex += 1
                break
            else:
                targetStartIndex = -1
                continue

def findNextIDandIndex(diskMap, currIndex):
    for i in range(currIndex, -1, -1):
        if diskMap[i] != '.':
            return diskMap[i], i
        else:
            continue
    return None, None

currId, endIndex = findNextIDandIndex(diskMap, len(diskMap) - 1)
if currId == None or endIndex == None:
    exit(-1)
startIndex = endIndex
for i in range(len(diskMap) - 1, -1, -1):
    if diskMap[i] != currId and diskMap[i] != '.':
        moveFile(diskMap, startIndex, endIndex)
        currId, endIndex = findNextIDandIndex(diskMap, i)
        if currId == None or endIndex == None:
            break
        startIndex = endIndex

    elif diskMap[i] == currId:
        startIndex = i
    else:
        continue




sum = 0
for index, value in enumerate(diskMap):
    if value == ".":
        continue
    valueInt = value
    sum += index * valueInt

print(sum)
