from itertools import pairwise
from functools import reduce

list1 = []

with open("2_input.txt", "r") as file:
    list1 = [list(map(int, line.split())) for line in file]

num_safe = 0
for i in list1:
    if i == sorted(i) or i == sorted(i, reverse=True):
        if 1 <= min(abs(x[0] - x[1]) for x in zip(i[1:], i)) <= max(abs(x[0] - x[1]) for x in zip(i[1:], i)) <= 3:
            num_safe += 1

print(num_safe)
