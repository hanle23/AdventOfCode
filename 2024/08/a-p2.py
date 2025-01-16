from aocd import get_data
data = get_data(day=8, year=2024)
data = data.splitlines()
WIDTH = len(data[0])
HEIGHT = len(data)

antennas = {}
for height in range(HEIGHT):
    for width in range(WIDTH):
        if 48 <= ord(data[height][width]) <= 57 or 65 <= ord(data[height][width]) <= 90 or 97 <= ord(data[height][width]) <= 122:
            if data[height][width] in antennas:
                antennas[data[height][width]].add((width, height))
            else:
                antennas[data[height][width]]= set([(width, height)])

antinodes = set()
for key, item in antennas.items():
    if len(item) <= 1:
        continue
    itemList = list(item)
    for index in range(len(itemList)):
        for innerIndex in range(len(itemList)):
            if innerIndex == index:
                continue
            delta = (itemList[innerIndex][0] - itemList[index][0], itemList[innerIndex][1] - itemList[index][1])
            currentPoints = [itemList[index]]
            for antenna in currentPoints:
                width, height = antenna[0] - delta[0],  antenna[1] - delta[1]
                if 0 <= width < WIDTH and 0 <= height < HEIGHT:
                    antinodes.add((width, height))
                    if (width, height) not in currentPoints:
                        currentPoints.append((width, height))
                width, height = antenna[0] + delta[0],  antenna[1] + delta[1]
                if 0 <= width < WIDTH and 0 <= height < HEIGHT:
                    antinodes.add((width, height))
                    if (width, height) not in currentPoints:
                        currentPoints.append((width, height))

print(len(antinodes))
