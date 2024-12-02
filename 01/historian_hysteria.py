from functools import reduce
from operator import add, sub

list1 = []
list2 = []

with open("1_input.txt", "r") as file:
    for line in file:
        x, y = map(int, line.split())
        list1.append(x)
        list2.append(y)

print(reduce(add,map(abs, map(sub, sorted(list1), sorted(list2)))))
