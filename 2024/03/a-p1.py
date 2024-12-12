from aocd import get_data
import re
data = get_data(day=3, year=2024)
p ="mul\(\d{1,3},\d{1,3}\)"
results = re.findall(p, data)
total = 0
for result in results:
    p = "\d{1,3}"
    numbers = re.findall(p, result)
    res = int(numbers[0]) * int(numbers[1])
    total += res

print(total)
