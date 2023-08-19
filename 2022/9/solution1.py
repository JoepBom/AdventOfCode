import numpy as np
import re
from pprint import pprint

# f = open("C:/Users/joep_/Documents/AdventOfCode/2022/9/input_small.txt", "r")
f = open("C:/Users/joep_/Documents/AdventOfCode/2022/9/input.txt", "r")
input = f.read().splitlines()
snake_length = 10
tail_positions = set()

def move_knot(head, tail):
    # print(head, tail)
    if head[0] == tail[0] and abs(head[1]-tail[1])>1:
        #horizontal
        tail[1] = tail[1] + (1 if head[1]>tail[1] else -1)
    elif head[1] == tail[1] and abs(head[0]-tail[0])>1:
        #vertical
        tail[0] = tail[0] + (1 if head[0]>tail[0] else -1)
    elif abs(head[0] - tail[0])>1 or abs(head[1] - tail[1])>1:
        #diagonal
        tail[1] = tail[1] + (1 if head[1]>tail[1] else -1)
        tail[0] = tail[0] + (1 if head[0]>tail[0] else -1)
    return tail

def update(snake, dir, amount):
    for _ in range(amount):
        if dir == "U":
            snake[0][0]+=1
        elif dir == "D":
            snake[0][0]-=1
        elif dir == "R":
            snake[0][1]+=1
        else:
            snake[0][1]-=1
        for i in range(1,len(snake)):
            snake[i] = move_knot(snake[i-1],snake[i])
        # print(snake)
        tail_positions.add(tuple(snake[-1]))
    return snake

snake = []
for _ in range(snake_length):
    snake.append([0,0])
tail_positions.add((0,0))
for i in input:
    inp = i.split(" ")
    snake = update(snake, inp[0], int(inp[1]))

print(len(tail_positions))
# print(sorted(tail_positions))
