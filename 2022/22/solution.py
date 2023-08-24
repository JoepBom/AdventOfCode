from pprint import pprint
import numpy as np
import random
import re
from itertools import combinations

file = open(r"C:\Users\JoepBom\Documents\AdventOfCode\2022\21\input.txt", "r")
input = file.readlines()
map = []
maxlen=len(input[9][:-1])
for i in input[:-2]:
    if len(i[:-1]) < maxlen:
        map.append((list(i[:-1])+[" "]*(maxlen-len(i[:-1]))))
    else:
        map.append(list(i[:-1]))
instructions = input[-1]
for i in map:
    print(i)

distances = re.split(r"L|R", instructions)
print(distances)
turns = re.findall(r"L|R", instructions)
print(turns)
positions=[]
position = [0,map[0].index("."),0]
print(position)
for i in range(len(distances)):
    if position[2] == 0:
        direction = [0,1]
    elif position[2] == 1:
        direction = [1,0]
    elif position[2] == 2:
        direction = [0,-1]
    elif position[2] == 3:
        direction = [-1,0]
    for j in range(int(distances[i])):
        dist=1
        while map[(position[0]+dist*direction[0])%len(map)][(position[1]+dist*direction[1])%len(map[position[0]])] == " ":
            dist+=1
        if map[(position[0]+dist*direction[0])%len(map)][(position[1]+dist*direction[1])%len(map[position[0]])] == "#":
            break
        if map[(position[0]+dist*direction[0])%len(map)][(position[1]+dist*direction[1])%len(map[position[0]])] == ".":
            position[0] += dist*direction[0]
            position[1] += dist*direction[1]
        position[0] %= len(map)
        position[1] %= len(map[position[0]])
        positions.append(position.copy())
    if i == len(distances)-1:
        break
    if turns[i] == "L":
        position[2] -= 1
    elif turns[i] == "R":
        position[2] += 1
    position[2] %= 4

for i in range(len(map)):
    for j in range(len(map[i])):
        if [i,j,0] in positions:
            print(">", end="")
        elif [i,j,1] in positions:
            print("v", end="")
        elif [i,j,2] in positions:
            print("<", end="")
        elif [i,j,3] in positions:
            print("^", end="")
        else:
            print(map[i][j], end="")
    print() 

print(1000*abs((1+position[0]))+4*abs((position[1]+1))+position[2])
