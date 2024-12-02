from aocd import get_data
from sortedcontainers import SortedList
data = get_data(day=1, year=2024)
dataList = data.split()
column1 = SortedList()
column2Occurance = {}
total = 0
for index in range(len(dataList)):
    if index % 2 == 0:
        column1.add(dataList[index])
    else:
        if dataList[index] in column2Occurance:
            column2Occurance[dataList[index]] +=1
        else:
            column2Occurance[dataList[index]] = 1

for num in column1:
    occurance = column2Occurance.get(num, 0)
    similarityScore = occurance * int(num)
    total += similarityScore
print(total)
