import re
from operator import add, mul
from functools import reduce

# Define the pattern
pattern = r"mul\((\d+),(\d+)\)"

with open("3_input.txt", "r") as file:
    text = file.read()

# Find all matches
matches = re.findall(pattern, text)

# Convert matches to tuples of integers
result = [(int(x), int(y)) for x, y in matches]

print(reduce(add, map((lambda x: mul(int(x[0]), int(x[1]))), matches)))

