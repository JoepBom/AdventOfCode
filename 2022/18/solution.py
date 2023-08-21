import numpy as np
import re
from pprint import pprint

f = open("C:/Users/joep_/Documents/AdventOfCode/2022/18/input", "r")
input = f.read().splitlines()
cubes = []
location_dict=dict()
for i in input:
    cubes.append([int(j) for j in i.split(",")])
for cube in cubes:
    if cube[0] not in location_dict.keys():
        location_dict[cube[0]]=dict()
    if cube[1] not in location_dict[cube[0]].keys():
        location_dict[cube[0]][cube[1]]=dict()
    location_dict[cube[0]][cube[1]][cube[2]]=True

def evaluate_cube(cube):
    surface=0
    for i in (-1, 1):
        for direction in (0,1,2):
            try: 
                location_dict[cube[0]+(i if direction==0 else 0)][cube[1]+(i if direction==1 else 0)][cube[2]+(i if direction==2 else 0)]
            except:
                surface+=1
    return surface

print(f"total surface: {sum((evaluate_cube(cube) for cube in cubes))}")


def evaluate_cube_outside(cube):
    for i in (-1, 1):
        for direction in (0,1,2):
            try: 
                outside_squares[cube[0]+(i if direction==0 else 0)][cube[1]+(i if direction==1 else 0)][cube[2]+(i if direction==2 else 0)]
                return True
            except:
                None
    return False

outside_squares=dict()
for x in (min(cube[0] for cube in cubes)-1, max(cube[0] for cube in cubes)+1):
    for y in (min(cube[1] for cube in cubes)-1, max(cube[1] for cube in cubes)+1):
        for z in (min(cube[2] for cube in cubes)-1, max(cube[2] for cube in cubes)+1):
            if x not in outside_squares.keys():
                outside_squares[x]=dict()
            if y not in outside_squares[x].keys():
                outside_squares[x][y]=dict()
            outside_squares[x][y][z]=True

pprint(outside_squares)
length_changed=True

while length_changed:
    length_changed=False
    for x in range(min(cube[0] for cube in cubes)-1, max(cube[0] for cube in cubes)+2):
        for y in range(min(cube[1] for cube in cubes)-1, max(cube[1] for cube in cubes)+2):
            for z in range(min(cube[2] for cube in cubes)-1, max(cube[2] for cube in cubes)+2):
                try: 
                    location_dict[x][y][z]
                except:
                    if evaluate_cube_outside([x,y,z]):
                        if x not in outside_squares.keys():
                            outside_squares[x]=dict()
                        if y not in outside_squares[x].keys():
                            outside_squares[x][y]=dict()
                        if z not in outside_squares[x][y].keys():
                            outside_squares[x][y][z]=True
                            length_changed=True
def evaluate_cube(cube):
    surface=0
    for i in (-1, 1):
        for direction in (0,1,2):
            try: 
                outside_squares[cube[0]+(i if direction==0 else 0)][cube[1]+(i if direction==1 else 0)][cube[2]+(i if direction==2 else 0)]
                surface+=1
            except:
                None
    return surface

print(f"total surface on the outside: {sum((evaluate_cube(cube) for cube in cubes))}")

quit