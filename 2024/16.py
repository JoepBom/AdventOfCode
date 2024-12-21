from aocd.models import Puzzle
from aocd import submit
import re

year=2024
day=16
puzzle = Puzzle(year,day)

input = puzzle.input_data.splitlines()
# input = puzzle.examples[0].input_data.splitlines()

walls = set()
for x, line in enumerate(input):
    for y, char in enumerate(line):
        if char == "#":
            walls.add((x,y))
        if char == "S":
            start = (x,y)
        if char == "E":
            end = (x,y)
# print(start, end)
min_dists = {((start[0], start[1]), (0,1)):[0, {start}]}

visited = set()
while True:
    # get the location and direction with minimum distance, that is not in visisted
    min_dist = 100000000000
    for loc, dir in min_dists:
        if (loc, dir) in visited:
            continue
        if min_dists[(loc,dir)][0] < min_dist:
            min_dist = min_dists[(loc,dir)][0]
            min_loc = loc
            min_dir = dir
    if min_dist == 100000000000:
        break
    if len([min_dists[(end, dir)][0] for loc, dir in min_dists if loc == end]) > 0 and min_dist >= min([min_dists[(end, dir)][0] for loc, dir in min_dists if loc == end]):
        break
    print(min_loc, min_dir, min_dist)
    for dir in ((0,1), (1,0), (0,-1), (-1,0)):
        if dir[0] == -min_dir[0] and dir[1] == -min_dir[1]:
            continue
        new_loc = (min_loc[0] + dir[0], min_loc[1] + dir[1])
        if new_loc in walls:
            continue
        if (new_loc, dir) not in min_dists:
            min_dists[(new_loc, dir)] = [min_dist + 1 + (1000 if dir != min_dir else 0), min_dists[(min_loc, min_dir)][1].union({new_loc})]
        else:
            if min_dist + 1 + (1000 if dir != min_dir else 0) < min_dists[(new_loc, dir)][0]:
                min_dists[(new_loc, dir)] = [min_dist + 1 + (1000 if dir != min_dir else 0), min_dists[(min_loc, min_dir)][1].union({new_loc})]
            elif min_dist + 1 + (1000 if dir != min_dir else 0) == min_dists[(new_loc, dir)][0]:
                min_dists[(new_loc, dir)][1] = min_dists[(new_loc, dir)][1].union(min_dists[(min_loc, min_dir)][1]).union({new_loc})
    # print(min_dists)
    visited.add((min_loc, min_dir))
    # print(visited)

# print(min_dists)
answer1 = min(min_dists[(end, dir)][0] for loc, dir in min_dists if loc == end)
# print([min_dists[(end, dir)] for loc, dir in min_dists if loc == end])
# print(answer1)

answer2_pos = set()

for loc, dir in min_dists:
    if loc == end:
        if min_dists[(loc, dir)][0] == answer1:
            answer2_pos = answer2_pos.union(min_dists[(loc, dir)][1])

answer2 = len(answer2_pos)
submit(answer1, part="a", day=day, year=year)
submit(answer2, part="b", day=day, year=year)
breakpoint()

