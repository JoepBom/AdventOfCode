from aocd.models import Puzzle
from aocd import submit
import re

year=2024
day=18
puzzle = Puzzle(year,day)

walls = list(tuple(int(j) for j in i.split(",")) for i in puzzle.input_data.splitlines())
# walls = set(tuple(int(j) for j in i.split(",")) for i in puzzle.examples[0].input_data.splitlines()[:1024])
# input = puzzle.examples[0].input_data.splitlines()
print(walls)
print(len(walls))
start = (0,0)
end = (70, 70)

min_i = 0
max_i = len(walls)

while True:
    if min_i == max_i or min_i == max_i - 1:
        break
    i = (min_i + max_i) // 2
    print(min_i, max_i, i)
    walls_tmp = walls[:i]

    min_dists = {(start[0], start[1]):0}
    visited = set()
    while True:
        # get the location with minimum distance, that is not in visisted
        min_dist = 100000000000
        for loc in min_dists:
            if loc in visited:
                continue
            if min_dists[loc] < min_dist:
                min_dist = min_dists[loc]
                min_loc = loc
        if min_dist == 100000000000:
            break
        if min_loc == end:
            break
        for dir in ((0,1), (1,0), (0,-1), (-1,0)):
            new_loc = (min_loc[0] + dir[0], min_loc[1] + dir[1])
            if new_loc in walls_tmp or new_loc[0]<0 or new_loc[1]<0 or new_loc[0]>end[0] or new_loc[1]>end[1]:
                continue
            if new_loc not in min_dists:
                min_dists[new_loc] = min_dist + 1
            else:
                if min_dist + 1 < min_dists[new_loc]:
                    min_dists[new_loc] = min_dist + 1
        visited.add(min_loc)
    if end in min_dists:
        min_i = i
        continue
    else:
        max_i = i
        continue

def print_map(walls,min_dists):
    for x in range(end[0]+1):
        for y in range(end[1]+1):
            if (x,y) in walls:
                print("#", end="")
            elif (x,y) in min_dists:
                print(min_dists[(x,y)]%10, end="")
            else:
                print(".", end="")
        print()

print_map(walls[:i], min_dists)
submit(",".join((str(i) for i in walls[min_i])), part="b", day=day, year=year)

