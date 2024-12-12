from aocd import get_data
import re
data = get_data(day=3, year=2024)
p ="mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"
results = re.findall(p, data)
newResult = []
flag = True
for result in results:
    if result == "do()":
        flag = True
    elif result == "don't()":
        flag = False
    else:
        if flag == True:
            newResult.append(result)
total = 0
for result in newResult:
    p = "\d{1,3}"
    numbers = re.findall(p, result)
    res = int(numbers[0]) * int(numbers[1])
    total += res

print(total)
