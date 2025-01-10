from aocd import get_data
import time
from functools import reduce
from operator import mul
t_start = time.process_time()
data = get_data(day=7, year=2024)
# data = '''190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20'''
data = data.splitlines()
splittedOperation = []

for equation in data:
   splitted = [equation.strip() for equation in equation.split(':')]
   splitted[0] = int(splitted[0])
   splitted[1] = [int(calibration) for calibration in splitted[1].split(" ")]
   splittedOperation.append(splitted)

print(f"reading data: {(time.process_time()-t_start)*1000:.3F} ms")
t_lap = time.process_time()

def recursion(prev, operators, index, target):
    if index == len(operators) and prev < target:
        return None
    elif index == len(operators) and prev > target:
        return None
    elif index == len(operators):
        return prev
    else:
        return recursion(prev + operators[index], operators, index + 1, target) or recursion(prev * operators[index], operators, index + 1, target) or recursion(int(str(prev) + str(operators[index])) , operators, index + 1, target)

sum = 0
for operation in splittedOperation:
    result, operators = operation
    # maximumResult = reduce(mul, operators)
    # if maximumResult < result:
    #     continue
    resultRecursion = recursion(operators[0], operators, 1, result)
    if resultRecursion != None:
        sum += result

t_round = time.process_time()
print(f"processing time: {(t_round-t_lap)*1000:.3F} ms")
print(f"total time elapsed: {(t_round-t_start)*1000:.3F} ms")
print(f"{sum} is the result.")
