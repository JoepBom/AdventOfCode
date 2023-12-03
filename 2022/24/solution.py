from pprint import pprint
import numpy as np
import random
import re
from itertools import combinations

file = open(r"C:\Users\JoepBom\Documents\AdventOfCode\2022\24\input.txt", "r")
input = file.readlines()
# (x,y,dx,dy)
blizzards = set()
walls = set()
for y, i in enumerate(input):
    for x, j in enumerate(i.strip()):
        if j == "#":
            walls.add((x,y))
        if j == ">":
            blizzards.add((x,y,1,0))
        if j == "<":
            blizzards.add((x,y,-1,0))
        if j == "^":
            blizzards.add((x,y,0,-1))
        if j == "v":
            blizzards.add((x,y,0,1))
walls.add((1,-1))
pprint(blizzards)
pprint(walls)
max_x = max(x for (x,y) in walls)
max_y = max(y for (x,y) in walls)
walls.add((max_x-1, max_y+1))

def move_blizzards(blizzards):
    new_blizzards = set()
    for blizzard in blizzards:
        new_blizzard = (((blizzard[0]+blizzard[2]-1)%(max_x-1))+1, ((blizzard[1]+blizzard[3]-1)%(max_y-1))+1, blizzard[2], blizzard[3])
        new_blizzards.add(new_blizzard)
    return new_blizzards

def print_blizzards(blizzards):
    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x,y) in walls:
                print("#", end="")
            elif (x,y) in {(i,j) for (i,j,_,_) in blizzards}:
                print("B", end="")
            else:
                print(".", end="")
        print()
positions = {(1,0)}
i=0
exit_found = False
while exit_found == False:
    i+=1
    blizzards=move_blizzards(blizzards)
    blizzard_locations = {(i,j) for (i,j,_,_) in blizzards}
    new_positions=set()
    for position in positions:
        if exit_found == True:
            break
        for movement in {(1,0), (-1,0), (0,1), (0,-1), (0,0)}:
            if (position[0]+movement[0], position[1]+movement[1]) not in blizzard_locations and (position[0]+movement[0], position[1]+movement[1]) not in walls:
                if (position[0]+movement[0], position[1]+movement[1]) == (max_x-1, max_y):
                    print("Found exit")
                    exit_found = True
                    print("steps: ", i)
                    break
                new_positions.add((position[0]+movement[0], position[1]+movement[1]))
    positions=new_positions
    # print("possible positions: ",len(positions))

positions = {(max_x-1, max_y)}
exit_found = False
while exit_found == False:
    i+=1
    blizzards=move_blizzards(blizzards)
    blizzard_locations = {(i,j) for (i,j,_,_) in blizzards}
    new_positions=set()
    for position in positions:
        if exit_found == True:
            break
        for movement in {(1,0), (-1,0), (0,1), (0,-1), (0,0)}:
            if (position[0]+movement[0], position[1]+movement[1]) not in blizzard_locations and (position[0]+movement[0], position[1]+movement[1]) not in walls:
                if (position[0]+movement[0], position[1]+movement[1]) == (1,0):
                    print("Found start")
                    exit_found = True
                    print("steps: ", i)
                    break
                new_positions.add((position[0]+movement[0], position[1]+movement[1]))
    positions=new_positions

positions = {(1,0)}
exit_found = False
while exit_found == False:
    i+=1
    blizzards=move_blizzards(blizzards)
    blizzard_locations = {(i,j) for (i,j,_,_) in blizzards}
    new_positions=set()
    for position in positions:
        if exit_found == True:
            break
        for movement in {(1,0), (-1,0), (0,1), (0,-1), (0,0)}:
            if (position[0]+movement[0], position[1]+movement[1]) not in blizzard_locations and (position[0]+movement[0], position[1]+movement[1]) not in walls:
                if (position[0]+movement[0], position[1]+movement[1]) == (max_x-1, max_y):
                    print("Found exit")
                    exit_found = True
                    print("steps: ", i)
                    break
                new_positions.add((position[0]+movement[0], position[1]+movement[1]))
    positions=new_positions
    # print("possible positions: ",len(positions))