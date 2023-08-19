import numpy as np
import re
from pprint import pprint

f = open("C:/Users/joep_/Documents/AdventOfCode/2022/8/input.txt", "r")
input = f.read().splitlines()
input = np.array([list(i) for i in input])

visible_trees = set()
max1 = -1
for i in range(len(input)):
    for j in range(0, len(input[i])):
        tree = int(input[i,j])
        if tree > max1:
            max1 = tree
            visible_trees.add((i,j))
    max1 = -1
    for j in range(len(input[i])-1, -1, -1):
        tree = int(input[i,j])
        if tree > max1:
            max1 = tree
            visible_trees.add((i,j))
    max1 = -1

for j in range(len(input[0])):
    for i in range(0, len(input)):
        tree = int(input[i,j])
        if tree > max1:
            max1 = tree
            visible_trees.add((i,j))
    max1 = -1
    for i in range(len(input)-1, -1, -1):
        tree = int(input[i,j])
        if tree > max1:
            max1 = tree
            visible_trees.add((i,j))
    max1 = -1

print(len(visible_trees))

scores = []     
for i in range(1,len(input)-1):
    for j in range(1,len(input[i])-1):
        score = 1
        cur_tree = int(input[i,j])
        for i1 in range(i+1, len(input)):
            if int(input[i1,j]) >= cur_tree or i1 == len(input)-1:
                score = score*(i1-i)
                break
        for i2 in range(i-1, -1, -1):
            if int(input[i2,j]) >= cur_tree or i2 == 0:
                score = score*(i-i2)
                break
        for j1 in range(j+1, len(input[i])):
            if int(input[i,j1]) >= cur_tree or j1 == len(input[i])-1:
                score = score*(j1-j)
                break
        for j2 in range(j-1, -1, -1):
            if int(input[i,j2]) >= cur_tree or j2 == 0:
                score = score*(j-j2)
                break
        scores.append(score)

print(max(scores))
    
