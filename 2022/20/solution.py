from pprint import pprint
import numpy as np
import random
from itertools import combinations

file = open(r"C:\Users\JoepBom\Documents\AdventOfCode\2022\19\input.txt", "r")
input = list((i, int(line)*811589153) for i, line in enumerate(file.readlines()))
pprint(input)

for k in range(10):
    for i in range(0, len(input)):
        index, node = list((j, input[j]) for j in range(0, len(input)) if input[j][0] == i)[0]
        # print(index, node)
        new_index = ((index + node[1]-1) % (len(input)-1))+1
        input.pop(index)
        input.insert(new_index, node)
        
    
# pprint(list(i[1] for i in input))
initial=list(i[1] for i in input).index(0)
print(input[(initial+1000)%len(input)][1]+input[(initial+2000)%len(input)][1]+input[(initial+3000)%len(input)][1])