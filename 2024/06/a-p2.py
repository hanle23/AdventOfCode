from aocd import get_data
data = get_data(day=6, year=2024)
# data = '''....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...'''
data = data.splitlines()

DIRECTIONS = ("^", "v", "<", ">")
TURN_90 = {"^":">", "v": "<", "<": "^", ">": "v"}
TO_ADD = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1)
}

def add_tuple(A,B):
    if len(A) != len(B):
        return None

    return tuple([A[i] + B[i] for i in range(len(A))])

def get_guard_position(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] in DIRECTIONS:
                return (i, j), map[i][j]
    return None, None

def get_obstacles(map):
    obstacles = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "#":
                obstacles.append((i, j))
    return obstacles

def is_outside(pos, dir, rows, cols):
    x, y = pos
    return any([
        (dir == "^" and x <= 0),
        (dir == "v" and x >= rows - 1),
        (dir == "<" and y <= 0),
        (dir == ">" and y >= cols - 1)
    ])

def add_pos(pos, dir):
    return add_tuple(pos, TO_ADD[dir])

def render(data, currentDirection = None, currentPosition = None, obstacle = None):
    renderData = data[:]
    # renderData[startingLocation[0]] = renderData[startingLocation[0]][:startingLocation[1]] + "." +  renderData[startingLocation[0]][startingLocation[1] + 1:]
    # renderData[currentPosition[0]] = renderData[currentPosition[0]][:currentPosition[1]] + str(currentDirection) +  renderData[currentPosition[0]][currentPosition[1] + 1:]
    # if obstacle:
    #     renderData[obstacle[0]] = renderData[obstacle[0]][:obstacle[1]] + "O" +  renderData[obstacle[0]][obstacle[1] + 1:]
    for i in range(len(data)):
        print(renderData[i])



def hasObstacleRightSide(map, dir, pos):
    mapCopy = map[:]
    rows, cols = len(mapCopy), len(mapCopy[0])
    posCopy = pos
    space = 1
    obstacles = get_obstacles(mapCopy)
    while not is_outside(posCopy, dir, rows, cols):
        nextPosition = add_pos(posCopy, dir)
        if nextPosition in obstacles and space >= 2:
            return True
        elif nextPosition in obstacles and space <= 1:
            return False
        posCopy = nextPosition
        space += 1
    return False

def run_path(map,obstacles):
    if map == None:
        return None
    mapCopy = map[:]
    rows, cols = len(mapCopy), len(mapCopy[0])
    # obstacles = get_obstacles(mapCopy)
    visited_obstacles = []
    pos, dir = get_guard_position(mapCopy)
    if pos == None or dir == None:
        return None
    visited = [[pos, dir]]
    is_loop = False
    while not is_outside(pos, dir, rows, cols):
        nextPosition = add_pos(pos, dir)
        if nextPosition in obstacles:
            if (nextPosition, dir) in visited_obstacles:
                is_loop = True
                break
            visited_obstacles.append((nextPosition, dir))
            dir = TURN_90[dir]
            nextPosition = add_pos(pos, dir)
        pos = nextPosition
        if [pos, dir] not in visited:
            visited.append([pos, dir])
    uniquePos = set()
    for pos in visited:
        uniquePos.add(pos[0])
    return len(list(uniquePos)), visited, is_loop

def process_path(map, coords, obstacles):
    # map, coords = args
    i, j= coords
    newMap = map[:]
    if newMap == None:
        return None
    if newMap[i][j] in DIRECTIONS:
        return 0
    newMap[i] = newMap[i][:j] + "#" +  newMap[i][j + 1:]
    obstaclesNew = obstacles[:]
    obstaclesNew.append(coords)
    _, _, is_loop = run_path(newMap, obstaclesNew)
    return 1 if is_loop else 0




obstacles = get_obstacles(data)
length, positions, _ = run_path(data,obstacles)
result = 0
print ("hello")
for index in range(1,len(positions)):
    pos, dir = positions[index]
    if index + 1 < len(positions):
        nextPos, nextDir = positions[index + 1]
        if nextDir != dir and pos == nextPos:
            continue
        rightSideDir = TURN_90[dir]
        rightSideHaveObstacle = hasObstacleRightSide(data, rightSideDir, pos)
        if rightSideHaveObstacle:
            print(pos, flush=True)
            isLooped = process_path(data, nextPos, obstacles)
            if isLooped != None:
                result += isLooped
                print(result, flush=True)

print(result, flush=True)





# All possible placement can be in any direction of any visited point
# No need to try all possible location in the map
# Can constantly looking to the next direction to see if there will be a block in that direction
# Need to skip one position after changing direction after start scanning
