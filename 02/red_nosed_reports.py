from itertools import pairwise
from functools import reduce

list1 = []

with open("2_input.txt", "r") as file:
    list1 = [list(map(int, line.split())) for line in file]

def is_safe(i):
    if i == sorted(i) or i == sorted(i, reverse=True):
        if 1 <= min(abs(x[0] - x[1]) for x in zip(i[1:], i)) <= max(abs(x[0] - x[1]) for x in zip(i[1:], i)) <= 3:
            return True
    return False

def is_tolerated(j):
    for i in range(len(j)):
        if is_safe(j[:i] + j[i+1:]):
            return True
    return False

print(sum(is_safe(l) for l in list1))
print(sum(is_safe(l) or is_tolerated(l) for l in list1))