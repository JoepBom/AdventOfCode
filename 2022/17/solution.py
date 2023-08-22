from pprint import pprint
import numpy as np
import random
from itertools import combinations

file = open(r"C:\Users\JoepBom\Documents\AdventOfCode\2022\17\input.txt", "r")
movement = []
for line in file.readlines():
    movement=line


shapes = (
    ((0,0),(1,0),(2,0),(3,0)),
    ((1,0),(0,1),(1,1),(2,1),(1,2)),
    ((0,0),(1,0),(2,0),(2,1),(2,2)),
    ((0,0),(0,1),(0,2),(0,3)),
    ((0,0),(1,0),(0,1),(1,1))
)
pprint(shapes)
shape_counter = -1
def get_next_shape():
    global shape_counter
    shape_counter+=1
    return list(shapes[shape_counter%len(shapes)])

movement_counter = -1
def get_next_movement():
    global movement_counter
    movement_counter+=1
    return movement[movement_counter%len(movement)]

highest_rock=0
rocks = set()
def move_current_shape(shape, movement):
    global highest_rock
    if movement==">":
        direction = 1
    elif movement=="<":
        direction = -1
    new_shape = []
    movement_possible = True
    for i in shape:
        if (i[0]+direction, i[1]) in rocks or i[0]+direction<0 or i[0]+direction>6:
            movement_possible = False
            new_shape = shape
            break
        new_shape.append((i[0]+direction, i[1]))
    movement_possible = True
    newest_shape = []
    for i in new_shape:
        if (i[0], i[1]-1) in rocks or i[1]-1<=0:
            movement_possible = False
            newest_shape = new_shape
            break
        newest_shape.append((i[0], i[1]-1))
    if not movement_possible:
        for i in newest_shape:
            rocks.add(i)
            if i[1]>highest_rock:
                highest_rock=i[1]
        return None
    return newest_shape

def start_new_shape(shape):
    global highest_rock
    new_shape=[]
    for i in shape:
        new_shape.append((i[0]+2, i[1]+4+highest_rock))
    return new_shape

cur_shape = None

def print_rocks():
    for y in range(highest_rock+1, highest_rock-10, -1):
        for x in range(0, 7):
            if (x, y) in rocks:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print("--------")
    for y in range(10, 0, -1):
        for x in range(0, 7):
            if (x, y) in rocks:
                print("#", end="")
            else:
                print(".", end="")
        print()

# while shape_counter<len(movement):
#     if cur_shape == None:
#         # print(movement_counter)
#         # print_rocks()
#         cur_shape = start_new_shape(get_next_shape())
#     cur_shape=move_current_shape(cur_shape, get_next_movement())
# print()
# print(len(rocks))
# print(shape_counter)
# print(movement_counter)
# print(highest_rock)

goal = 1000000000000
# goal = 2022


print(len(movement))
print()
prev_movement_shape_combinations = dict()
while shape_counter<goal:
    if cur_shape == None:
        if ((movement_counter)%len(movement), (shape_counter)%len(shapes)) in prev_movement_shape_combinations.keys() and shape_counter>2000:
            print("repetitive")
            print((movement_counter)%len(movement), (shape_counter)%len(shapes))
            repetitive_from = prev_movement_shape_combinations[((movement_counter)%len(movement), (shape_counter)%len(shapes))]
            repetitive_to = (movement_counter, shape_counter, highest_rock)
            print(movement_counter, shape_counter)
            break
        prev_movement_shape_combinations[((movement_counter)%len(movement), (shape_counter)%len(shapes))] = (movement_counter, shape_counter, highest_rock)
        cur_shape = start_new_shape(get_next_shape())
    cur_shape=move_current_shape(cur_shape, get_next_movement())
print(repetitive_from)
print(repetitive_to)
print_rocks()
print()
print()
cur_shape=start_new_shape(get_next_shape())
cur_shape=move_current_shape(cur_shape, get_next_movement())
cur_shape=move_current_shape(cur_shape, get_next_movement())
cur_shape=move_current_shape(cur_shape, get_next_movement())
cur_shape=move_current_shape(cur_shape, get_next_movement())
print_rocks()

rocks = set()
cur_shape = None
shape_counter = -1
movement_counter = -1
highest_rock=0


while shape_counter<((goal)%(repetitive_to[1]-repetitive_from[1])):
    if cur_shape == None:
        cur_shape = start_new_shape(get_next_shape())
    cur_shape=move_current_shape(cur_shape, get_next_movement())

highest_rock_repetitive = repetitive_to[2]-repetitive_from[2]



print(highest_rock_repetitive*(int((goal)/(repetitive_to[1]-repetitive_from[1])))+highest_rock)
# print(len(rocks))
# print(shape_counter)
# print(movement_counter)
# print(highest_rock)

# print(highest_rock_repetitive*(int(1000000000000/len(movement))-1)+highest_rock)


# WRONG
# 1594236311216

# CORRECT
# 1595988538691