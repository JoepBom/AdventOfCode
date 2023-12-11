import os
from aocd.models import Puzzle
from aocd import submit
import sys
from pprint import pprint
os.environ['AOC_SESSION'] = '53616c7465645f5f5274298a1513bd33b311098204a4e371d2880a4590e8a95748ea42877f6b28b349045dcc1fee6d10f00932890ec53d2fdfe8a068bae08242'

year=2023
day=10
part='a'

sys.setrecursionlimit(100000)

puzzle = Puzzle(year=year, day=day)
input = puzzle.input_data.splitlines()

pipe_map=dict()
for y, line in enumerate(input):
    for x, pipe in enumerate(input[y]):
        if pipe==".":
            continue
        else:
            pipe_map[(x,y)]=pipe
        if pipe=="S":
            start=(x,y)

shapes = {"|": [(0,1), (0,-1)], "-":[(1,0), (-1,0)], "L":[(1,0), (0,-1)], "F":[(1,0), (0,1)], "7":[(0,1), (-1,0)], "J":[(0,-1), (-1,0)], "S":[]}

distances={start:0}
def eval_step(pos, prev_pos, count):
    try:
        if distances[pos]>count:
            distances[pos]=count
        else:
            return
    except:
        distances[pos]=count
    for dir in shapes[pipe_map[pos]]:
        if dir[0]==prev_pos[0]-pos[0] and dir[1]== prev_pos[1]-pos[1]:
            continue
        return eval_step((pos[0]+dir[0], pos[1]+dir[1]), pos, count+1)
    return

for dir in ((0,1), (0,-1), (1,0), (-1,0)):
    if (start[0]-dir[0], start[1]-dir[1]) in pipe_map and dir in shapes[pipe_map[(start[0]-dir[0], start[1]-dir[1])]]:
        eval_step((start[0]-dir[0], start[1]-dir[1]), start, 1)

submit(max(distances.values()), year=year, day=day, part=part)

part='b'

bends = {pos: pipe_map[pos] for pos in distances if pipe_map[pos] in "LF7J|"}
bends[start]="J"

ans2=0
insides=set()
for y in range(min(pos[1] for pos in distances.keys()), max(pos[1] for pos in distances.keys())+1):
    inside=False
    prev_bend = None
    for x in range(min(pos[0] for pos in distances.keys()), max(pos[0] for pos in distances.keys())+1):
        if (x,y) in bends:
            if bends[(x,y)]=="|":
                inside=not inside
                continue
            if prev_bend is None:
                prev_bend = bends[(x,y)]
                continue
            if (prev_bend == "L" and bends[(x,y)]=="7") or (prev_bend == "F" and bends[(x,y)]=="J"):
                inside=not inside
                prev_bend = None
            if (prev_bend == "L" and bends[(x,y)]=="J") or (prev_bend == "F" and bends[(x,y)]=="7"):
                prev_bend = None
            continue
        if (x,y) not in distances and inside:
            ans2+=1
            insides.add((x,y))

submit(ans2, year=year, day=day, part=part)

for y in range(min(pos[1] for pos in distances.keys()), max(pos[1] for pos in distances.keys())+1):
    for x in range(min(pos[0] for pos in distances.keys()), max(pos[0] for pos in distances.keys())+1):
        if (x,y) in distances:
            print(pipe_map[(x,y)], end="")
        elif (x,y) in insides:
            print("O", end="")
        else:
            print(" ", end="")
    print()
