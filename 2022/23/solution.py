from pprint import pprint
import numpy as np
import random
import re
from itertools import combinations

file = open(r"C:\Users\JoepBom\Documents\AdventOfCode\2022\23\input.txt", "r")
input = file.readlines()
positions = set()
for y, i in enumerate(input):
    for x, j in enumerate(i.strip()):
        if j == "#":
            positions.add((x,y))
# pprint(positions)
directions = [((0,-1),(-1,-1),(1,-1)), ((0,1),(-1,1),(1,1)), ((-1,0),(-1,-1),(-1,1)), ((1,0),(1,-1),(1,1))]

def get_next_positions(positions, round):
    next_positions = dict()
    for position in positions:
        solo=True
        for i in range(4):
            direction = directions[(round+i)%4]
            if (not solo) and (position in next_positions.keys()):
                break
            if (
                (position[0]+direction[0][0], position[1]+direction[0][1]) in positions
                or (position[0]+direction[1][0], position[1]+direction[1][1]) in positions
                or (position[0]+direction[2][0], position[1]+direction[2][1]) in positions
            ):
                solo=False
                continue
            elif position not in next_positions.keys():
                next_positions[position] = (position[0]+direction[0][0], position[1]+direction[0][1])
        if solo or position not in next_positions.keys():
            next_positions[position] = position
    return next_positions

def remove_double_positions(next_positions):
    seen = set()
    double_positions = []
    for pos in next_positions.values():
        if pos in seen:
            double_positions.append(pos)
        else:
            seen.add(pos)
    positions = {(key if value in double_positions else value) for key, value in next_positions.items() }
    # pprint(next_positions)
    # print(double_positions)
    return positions
res=positions
for i in range(100000000000000):
    prev_res = res
    res = get_next_positions(res, i)
    res = remove_double_positions(res)
    if res == prev_res:
        break
    # pprint(res)
    # for y in range(min(y for x,y in res), max(y for x,y in res)+1):
    #     for x in range(min(x for x,y in res), max(x for x,y in res)+1):
    #         if (x,y) in res:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print()
print((max(y for x,y in res)+1-min(y for x,y in res))*(max(x for x,y in res)+1-min(x for x,y in res))-len(res))
print(i+1)
