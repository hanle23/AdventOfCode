from aocd import get_data
data = get_data(day=6, year=2024)
data = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
data = data.splitlines()
HEIGHT = len(data)
WIDTH = len(data[0])

# All possible facing and direction
directions = [(1,0), (0,-1), (-1,0), (0,1)]
possibleFacing = ["v", "<", "^", ">"]


# Finding starting position and starting direction
startingDirection = None
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
            startingDirection = possibleFacing.index(data[i][j])

if currentPosition == None or currentDirectionIndex == None:
    print("Error: currentPositiona or currentDirection is Null")

def render(data, currentDirection, currentPosition):
    renderData = data[:]
    renderData[currentPosition[0]] = renderData[currentPosition[0]][:currentPosition[1]] + currentDirection +  renderData[currentPosition[0]][currentPosition[1] + 1:]
    for i in range(len(data)):
        print(renderData[i])
    print("-" * len(data[0]))



visited = []
possiblePlacement = set()
flag = True
while flag:
    if currentPosition == None or currentDirectionIndex == None:
        flag = False
        continue
    visited.append(currentPosition)
    nextPosition = (currentPosition[0] + directions[currentDirectionIndex][0],currentPosition[1] + directions[currentDirectionIndex][1])
    if nextPosition[0] < 0 or nextPosition[0] >= HEIGHT or nextPosition[1] < 0 or nextPosition[1] >= WIDTH:
        flag = False
        continue
    if data[nextPosition[0]][nextPosition[1]] == "#":
        currentDirectionIndex = (currentDirectionIndex + 1) % len(directions)
    else:
        currentPosition = nextPosition


# All possible placement can be in any direction of any visited point
# No need to try all possible location in the map
# Can constantly looking to the next direction to see if there will be a block in that direction
# Need to skip one position after changing direction after start scanning
