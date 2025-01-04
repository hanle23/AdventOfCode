from aocd import get_data
import math
data = get_data(day=5, year=2024)
data = data.splitlines()

# For each rules, i0 goes before i1
rules = []
rulesBook = {}
updates = []
for line in data:
    if "|" in line:
        line = [x.strip() for x in line.split('|')]
        rules.append(line)
    elif line == "":
        continue
    else:
        updates.append(line)

for rule in rules:
    if int(rule[1]) in rulesBook:
        rulesBook[int(rule[1])].add(int(rule[0]))
    else:
        rulesBook[int(rule[1])] = set([int(rule[0])])

def checkValid(pages):
    disallowed = set()
    for page in pages:
        currPage = int(page)
        if currPage in disallowed:
            return False
        disallowed |= rulesBook[currPage]
    return True

sum = 0
for update in updates:
    curr = update.split(",")
    isValid = checkValid(curr)
    if not isValid:
        continue
    sum += int(curr[len(curr) // 2])

print(sum)
