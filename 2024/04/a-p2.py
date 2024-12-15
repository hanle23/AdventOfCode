from aocd import get_data
data = get_data(day=4, year=2024)
data = data.splitlines()
for index in range(0, len(data)):
    data[index] = list(data[index])

directions = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
total = 0

for r in range(0, len(data)):
    for c in range(0, len(data[0])):
        if data[r][c] != "A":
            continue
        if r + 1 >= len(data) or r - 1 < 0 or c + 1 >= len(data[0]) or c - 1 < 0:
            continue
        if data[r + 1][c + 1] == "S" and data[r - 1][c - 1] == "M" and data[r + 1][c - 1] == "S" and data[r - 1][c + 1] == "M":
            total += 1
        if data[r + 1][c + 1] == "S" and data[r - 1][c - 1] == "M" and data[r + 1][c - 1] == "M" and data[r - 1][c + 1] == "S":
            total += 1
        if data[r + 1][c + 1] == "M" and data[r - 1][c - 1] == "S" and data[r + 1][c - 1] == "M" and data[r - 1][c + 1] == "S":
            total += 1
        if data[r + 1][c + 1] == "M" and data[r - 1][c - 1] == "S" and data[r + 1][c - 1] == "S" and data[r - 1][c + 1] == "M":
            total += 1
print(total)
