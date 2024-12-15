from aocd import get_data
data = get_data(day=4, year=2024)
data = data.splitlines()
for index in range(0, len(data)):
    data[index] = list(data[index])

directions = [[1, 0], [0, 1], [-1,0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
target = "XMAS"
# If index == "X", start finding
# If index == "X", loop from 0, len
total = 0

def DFS(r, c, index, direction):
    if index == 4:
        return 1
    if r >= len(data) or r < 0 or c >= len(data[0]) or c < 0 or data[r][c] != target[index]:
        return 0
    row, col = direction
    return DFS(r + row, c + col, index + 1, direction)

for r in range(0, len(data)):
    for c in range(0, len(data[r])):
        if data[r][c] == "X":
            for direction in directions:
                row, col = direction
                total += DFS(r + row, c + col, 1, direction)

print(total)
