import numpy
from pprint import pprint
# f = open("C:/Users/joep_/Documents/AdventOfCode/2020/18/input copy.txt", "r")
f = open("C:/Users/joep_/Documents/AdventOfCode/2020/18/input.txt", "r")
input=f.read().splitlines()
print(input)


tail_positions = set()
def update(head_tup, tail_tup, dir, amount):
    for i in amount:
        if dir == "U":
            head_tup[0]+=1
            if head_tup[0]-tail_tup[0]>1:
                tail_tup = (head_tup[0]-1, head_tup[1])
        elif dir == "D":
            head_tup[0]-=1
            if tail_tup[0]-head_tup[0]>1:
                tail_tup = (head_tup[0]+1, head_tup[1])
        elif dir == "R":
            head_tup[1]+=1
            if head_tup[1]-tail_tup[1]>1:
                tail_tup = (head_tup[0], head_tup[1]-1)
        else:
            head_tup[1]==1
            if tail_tup[1]-head_tup[1]>1:
                tail_tup = (head_tup[0], head_tup[1]+1)
        tail_positions.add(tail_tup)
    return head_tup, tail_tup


head = (0,0)
tail = (0,0)
for i in input:
    inp = i.split(" ")
    update(head, tail, inp[0], int(inp[1]))

print(len(tail_positions))