from pathlib import Path
import importlib.util
import math

# Import util.util from the parent directory
util_path = Path(__file__).parent.parent.parent / 'util' / 'util.py'
spec = importlib.util.spec_from_file_location('util.util', util_path)
util_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(util_module)

# Import functions from the module
get_test_data = util_module.get_test_data
get_data = util_module.get_data


data = get_data().split("\n")
current_point = 50
count = 0

for line in data:
    if not line:
        continue
    direction = line[0]
    distance = line[1:]

    if direction == "L":
        if current_point == 0:
            count += int(distance) // 100
        elif int(distance) >= current_point:
            count += (int(distance) - current_point) // 100 + 1
        current_point = ((current_point - int(distance)) % 100)
    else:
        count += ((current_point + int(distance)) // 100)
        current_point = ((current_point + int(distance)) % 100)

print(count)
