from aocd import get_data
data = get_data(day=5, year=2024)
data = data.splitlines()
rules =[]
updates = []
for line in data:
    if "|" in line:
        line = [int(x.strip()) for x in line.split('|')]
        rules.append(line)
    else:
        updates.append(line)

print(rules)
print(updates)
