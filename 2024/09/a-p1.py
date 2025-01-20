from aocd import get_data
data = get_data(day=9, year=2024)
diskMap = []
id = 0
for i in range(len(data)):
    size = int(data[i])
    if i % 2 == 0:
        temp = [str(id)] * size
        diskMap.extend(temp)
        id += 1
    else:
        temp = ["."] * size
        diskMap.extend(temp)
result = ""
start, end = 0, len(diskMap) - 1
while diskMap[end] == "." and end != start:
    end -= 1

while start != end:
    if diskMap[start] == ".":
        diskMap[start], diskMap[end] = diskMap[end], diskMap[start]
        start += 1
    else:
        start += 1
    if diskMap[end] == ".":
        while diskMap[end] == "." and end != start:
            end -= 1

sum = 0
for index, value in enumerate(diskMap):
    if value == ".":
        continue
    valueInt = int(value)
    sum += index * valueInt

print(sum)
