from pprint import pprint
import numpy as np
import random
import re
from itertools import combinations
from copy import deepcopy

file = open(r"C:\Users\JoepBom\Documents\AdventOfCode\2022\22\input.txt", "r")
input = file.readlines()
map = []
maxlen=len(input[9][:-1])
instructions = input.pop()
input.pop()
area_size = len(input)//4

areas=dict()
for y in range(len(input)):
    if y%area_size == 0:
        areas[y//area_size]=dict()
    for x in range(len(input[y])-1):
        if x%area_size == 0 and y%area_size == 0:
            areas[y//area_size][x//area_size] = set()
        if input[y][x] == "#":
            areas[y//area_size][x//area_size].add((x%area_size,y%area_size))

todel=[]
for y in areas:
    for x in areas[y]:
        if len(areas[y][x]) == 0:
            todel.append((x,y))

for i in todel:
    del areas[i[1]][i[0]]
for y in areas:
    for x in areas[y]:
        print(len(areas[y][x]))
    print()

area_ids = {(x,y) for y in areas for x in areas[y]}


class Area:
    neighbours = dict()
    blockades = set()

    def __init__(self, id, blockades):
        self.id = id
        self.neighbours = dict()
        self.blockades = blockades

    def add_neighbour(self, neighbour, direction, turn):
        self.neighbours[direction] = (neighbour, turn)

Areas = dict()
for y in areas:
    for x in areas[y]:
        Areas[(x,y)]=Area((x,y), areas[y][x])

max_x = 4
max_y = 4
print(max_x, max_y)
for (x,y), area in Areas.items():
    if ((x+1)%max_x,y) in area_ids:
        area.add_neighbour(Areas[((x+1)%max_x,y)], "R", "U")
    if ((x-1)%max_x,y) in area_ids:
        area.add_neighbour(Areas[((x-1)%max_x,y)], "L", "U")
    if (x,(y+1)%max_y) in area_ids:
        area.add_neighbour(Areas[(x,(y+1)%max_y)], "D", "U")
    if (x,(y-1)%max_y) in area_ids:
        area.add_neighbour(Areas[(x,(y-1)%max_y)], "U", "U")

for (x,y), area in Areas.items():
    print(area.id, {key: [val[0].id, val[1]] for key,val in area.neighbours.items()})
    
turn = {"U": {"U": "U", "L": "L", "R": "R", "D": "D"},
        "L": {"U": "L", "L": "D", "R": "U", "D": "R"},
        "R": {"U": "R", "L": "U", "R": "D", "D": "L"},
        "D": {"U": "D", "L": "R", "R": "L", "D": "U"}}
rev_turn = {"U": {"U": "U", "L": "L", "R": "R", "D": "D"},
        "L": {"U": "R", "L": "U", "R": "D", "D": "L"},
        "R": {"U": "L", "L": "D", "R": "U", "D": "R"},
        "D": {"U": "D", "L": "R", "R": "L", "D": "U"}}

while sum(len(area.neighbours) for area in Areas.values()) < 4*len(Areas):
    for (i,j), area in Areas.items():
        for dir in "U", "D", "L", "R":
            if dir in area.neighbours:
                continue
            if turn["R"][dir] in area.neighbours and rev_turn[area.neighbours[turn["R"][dir]][1]][dir] in area.neighbours[turn["R"][dir]][0].neighbours:
                x=area.neighbours[turn["R"][dir]][0].neighbours[rev_turn[area.neighbours[turn["R"][dir]][1]][dir]]
                area.add_neighbour(x[0], dir, turn["L"][turn[area.neighbours[turn["R"][dir]][1]][x[1]]])
                continue
            if turn["L"][dir] in area.neighbours and rev_turn[area.neighbours[turn["L"][dir]][1]][dir] in area.neighbours[turn["L"][dir]][0].neighbours:
                x=area.neighbours[turn["L"][dir]][0].neighbours[rev_turn[area.neighbours[turn["L"][dir]][1]][dir]]
                area.add_neighbour(x[0], dir, turn["R"][turn[area.neighbours[turn["L"][dir]][1]][x[1]]])
                continue
            
for (i,j), area in Areas.items():
    print(area.id, {key: [val[0].id, val[1]] for key,val in area.neighbours.items()})

direction_map = {"U": [0,-1], "D": [0,1], "L": [-1,0], "R": [1,0]}


distances = re.split(r"L|R", instructions)
# print(distances)
turns = re.findall(r"L|R", instructions)
# print(turns)
positions=[]
first_area = Areas[(min(x for x,y in Areas if y==0),0)]
position = [first_area.id,[min(x for x in range(area_size) if (x,0) not in first_area.blockades),0],"R"]
print(position)
for i in range(len(distances)):
    for j in range(int(distances[i])):
        direction = direction_map[position[2]]
        nb = None
        next_position = deepcopy(position)
        next_position[1][0] += direction[0]
        next_position[1][1] += direction[1]
        if next_position[1][0] >= area_size:
            nb = "R"
        elif next_position[1][0] < 0:
            nb = "L"
        elif next_position[1][1] >= area_size:
            nb = "D"
        elif next_position[1][1] < 0:
            nb = "U"
        if nb is not None:
            next_position[1][0] = next_position[1][0]%area_size
            next_position[1][1] = next_position[1][1]%area_size
            if Areas[position[0]].neighbours[nb][1] == "R":
                next_position[1] = [next_position[1][1], area_size-1-next_position[1][0]]
            elif Areas[position[0]].neighbours[nb][1] == "L":
                next_position[1] = [area_size-1-next_position[1][1], next_position[1][0]]
            elif Areas[position[0]].neighbours[nb][1] == "D":
                next_position[1] = [area_size-1-next_position[1][0], area_size-1-next_position[1][1]]
            next_position[2] = rev_turn[Areas[position[0]].neighbours[nb][1]][next_position[2]]
            next_position[0] = Areas[position[0]].neighbours[nb][0].id
        if (next_position[1][0], next_position[1][1]) in Areas[next_position[0]].blockades:
            break
        position = deepcopy(next_position)
        print(position)
        positions.append([next_position[0][0]*area_size+next_position[1][0], next_position[0][1]*area_size+next_position[1][1], next_position[2]])
    if i == len(distances)-1:
        break
    position[2] = turn[position[2]][turns[i]]

print(positions)


for y in range(len(input)):
    for x in range(len(input[y])):
        if x==positions[-1][0] and y==positions[-1][1]:
            print("X", end="")
            continue
        if [x,y,"R"] in positions:
            print(">", end="")
        elif [x,y,"D"] in positions:
            print("v", end="")
        elif [x,y,"L"] in positions:
            print("<", end="")
        elif [x,y,"U"] in positions:
            print("^", end="")
        elif input[y][x] == "#":
            print("#", end="")
        else:
            print(" ", end="")
    print() 

print(abs((position[0][0]*area_size + position[1][0]+1)), abs((position[0][1]*area_size+position[1][1]+1)), position[2])
print(1000*abs((position[0][1]*area_size+position[1][1]+1))+4*abs((position[0][0]*area_size + position[1][0]+1))+(0 if position[2]=="R" else 1 if position[2]=="D" else 2 if position[2]=="L" else 3))
