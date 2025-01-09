# Credit to topaz
from sys import argv
import time
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
map = data.splitlines()

t_start = time.process_time()

directions = [(0,-1), (1,0), (0,1), (-1,0)]
DIRECTIONS = {
    "^": 3,
    "v": 1,
    ">": 2,
    "<": 0
}

print(f"reading data: {(time.process_time()-t_start)*1000:.3F} ms")
t_lap = time.process_time()

WIDTH, HEIGHT = (len(map[0]), len(map))
def outside(x,y):
    return not (0<=x<WIDTH and 0<=y<HEIGHT)

neighbor = dict()
obstacles = set()
nodes = [(width, height, sides) for width in range(WIDTH) for height in range(HEIGHT) for sides in range(4)]
startpos = None
for width,height in [(width,height) for width in range(WIDTH) for height in range(HEIGHT)]:
    if map[height][width] == "#":
        obstacles.add((width,height))
    elif map[height][width] in DIRECTIONS:
        startpos = (width, height, DIRECTIONS[map[height][width]])

if startpos == None:
    raise ValueError

for width, height, sides in nodes:
    if outside(width + directions[sides][0], height + directions[sides][1]):
        neighbor[(width, height, sides)] = (-1,-1,-1)
    elif (width + directions[sides][0], height + directions[sides][1]) in obstacles:
        neighbor[(width, height, sides)] = (width, height, (sides + 1) % len(directions))
    else:
        neighbor[(width, height, sides)] = (width + directions[sides][0], height + directions[sides][1], sides)

print(f"processing nodes: {(time.process_time()-t_lap)*1000:.3F} ms")
t_lap = time.process_time()

orig_path = []
orig_visited = set()

pos = startpos
while not pos == (-1,-1,-1):
    orig_path.append(pos)
    orig_visited.add((pos[0], pos[1]))
    pos = neighbor[pos]

print(f"walking path: {(time.process_time()-t_lap)*1000:.3F} ms")
print(f"path has {len(orig_path)} steps on {len(orig_visited)} unique nodes")

loop_obstacles = set()
for index, pos in enumerate(orig_path[1:],1):
    width, height = (pos[0], pos[1])
    if (width, height) in loop_obstacles:
        continue
    for sides in range(len(directions)):
        prev = (width - directions[sides][0], height - directions[sides][1], sides)
        neighbor[prev] = (prev[0], prev[1], (sides + 1) % len(directions))
    visited = set()
    cur = orig_path[index - 1]
    while cur != (-1,-1,-1) and cur not in visited:
        visited.add(cur)
        cur = neighbor[cur]
    if cur != (-1,-1,-1):
        loop_obstacles.add((pos[0],pos[1]))
    for sides in range(len(directions)):
        prev = (width - directions[sides][0], height - directions[sides][1], sides)
        neighbor[prev] = (pos[0], pos[1], sides)

t_round1 = time.process_time()
print(f"checking for obstacles: {(t_round1-t_lap)*1000:.3F} ms")
print(f"total time elapsed: {(t_round1-t_start)*1000:.3F} ms")
print(f"{len(loop_obstacles)} obstacles lead to a loop.")
