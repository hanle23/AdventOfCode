from aocd import get_data
import time
t_start = time.process_time()
data = get_data(day=9, year=2024)
print(f"reading data: {(time.process_time()-t_start)*1000:.3F} ms")
t_lap = time.process_time()
diskMap = []
id = 0
for i in range(len(data)):
    size = int(data[i])
    if i % 2 == 0:
        temp = [id] * size
        diskMap.extend(temp)
        id += 1
    else:
        temp = ["."] * size
        diskMap.extend(temp)
print(f"processing time: {(time.process_time()-t_lap)*1000:.3F} ms")
t_round = time.process_time()
result = ""
start, end = 0, len(diskMap) - 1
while diskMap[end] == "." and end != start:
    end -= 1

while start != end:
    if diskMap[start] == ".":
        diskMap[start], diskMap[end] = diskMap[end], diskMap[start]
        start += 1
    else:
        start += 1
    if diskMap[end] == ".":
        while diskMap[end] == "." and end != start:
            end -= 1
print(f"processing time 2: {(time.process_time()-t_round)*1000:.3F} ms")
t_round = time.process_time()
sum = 0
processTime = 0
for index, value in enumerate(diskMap):
    if value == ".":
        continue
    sum += index * value
t_end = time.process_time()
print(f"counting points linear time: {(t_end-t_round)*1000:.3F} ms")
print(sum)
