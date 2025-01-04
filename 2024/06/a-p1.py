from aocd import get_data
data = get_data(day=6, year=2024)
data = data.splitlines()
HEIGHT = len(data)
WIDTH = len(data[0])

# All possible facing and direction
directions = [(1,0), (0,-1), (-1,0), (0,1)]
possibleFacing = ["v", "<", "^", ">"]


# Finding starting position and starting direction
currentDirectionIndex = None
currentPosition = None
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] not in possibleFacing:
            continue
        if not currentPosition:
            currentPosition = (i,j)
        if not currentDirectionIndex:
            currentDirectionIndex = possibleFacing.index(data[i][j])

if currentPosition == None or currentDirectionIndex == None:
    print("Error: currentPositiona or currentDirection is Null")

visited = set()
flag = True
while flag:
    if currentPosition == None or currentDirectionIndex == None:
        flag = False
        continue
    if currentPosition not in visited:
        visited.add(currentPosition)
    nextPosition = (currentPosition[0] + directions[currentDirectionIndex][0],currentPosition[1] + directions[currentDirectionIndex][1])
    if nextPosition[0] < 0 or nextPosition[0] >= HEIGHT or nextPosition[1] < 0 or nextPosition[1] >= WIDTH:
        flag = False
        continue
    if data[nextPosition[0]][nextPosition[1]] == "#":
        currentDirectionIndex = (currentDirectionIndex + 1) % len(directions)
    else:
        currentPosition = nextPosition
    # Checking for break condition


print(len(visited))
