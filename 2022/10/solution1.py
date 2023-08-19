import numpy as np
import re
from pprint import pprint

# f = open("C:/Users/joep_/Documents/AdventOfCode/2022/10/input_small.txt", "r")
f = open("C:/Users/joep_/Documents/AdventOfCode/2022/10/input.txt", "r")
input = f.read().splitlines()
cur_cycle = 0
X = 1
tot = 0

drawing = ""

for i in input:
    drawing+=("#" if X-1 <= (cur_cycle%40) <= X+1 else ".")
    cur_cycle += 1
    if cur_cycle in [20,60,100,140,180,220]:
        tot += cur_cycle * X
    if i == "noop":
        continue
    if i[:4] == "addx":
        drawing+=("#" if X-1 <= (cur_cycle%40) <= X+1 else ".")
        cur_cycle += 1
        if cur_cycle in [20,60,100,140,180,220]:
            tot += cur_cycle * X
        X += int(i[5:])

print(tot)
for i in range(8):
    print(drawing[i*40:(i+1)*40])

