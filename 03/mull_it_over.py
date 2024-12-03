import re
from operator import add, mul
from functools import reduce

def mul_tuples(tuplist):
    return reduce(add, map((lambda x: mul(int(x[0]), int(x[1]))), tuplist))

text = ""
with open("3_input.txt", "r") as file:
    text = file.read()

clean_text = "".join([segment[segment.find("do()") :] for segment in ("do()" + text).split("don't()")])
# Find all matches
pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, text)
only_do = re.findall(pattern, clean_text)

print(mul_tuples(matches))
print(mul_tuples(only_do))

