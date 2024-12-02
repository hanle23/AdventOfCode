from aocd import get_data
from sortedcontainers import SortedList
data = get_data(day=1, year=2024)
dataList = data.split()
column1 = SortedList()
column2 = SortedList()
total = 0
for index in range(len(dataList)):
    if index % 2 == 0:
        column1.add(dataList[index])
    else:
        column2.add(dataList[index])

for index in range(len(column1)):
    curr = abs(int(column1[index]) - int(column2[index]))
    total += curr
print(total)
