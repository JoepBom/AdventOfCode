from aocd.models import Puzzle
from aocd import submit
import copy

year=2024
day=6
puzzle = Puzzle(year,day)

map = puzzle.input_data.splitlines()

rocks = {x: set() for x in range(len(map))}
for x in range(len(map)):
    for y in range(len(map[0])):
        if map[x][y] == "#":
            rocks[x].add(y)
        elif map[x][y] == "^":
            guard_pos_init = (x,y)
            guard_dir_init = (-1,0)

guard_pos = guard_pos_init
guard_dir = guard_dir_init

def move_guard(guard_pos, guard_dir, rocks):
    if guard_pos[0]+guard_dir[0] in rocks and guard_pos[1]+guard_dir[1] in rocks[guard_pos[0]+guard_dir[0]]:
        guard_dir = (guard_dir[1], -guard_dir[0])
        return move_guard(guard_pos, guard_dir, rocks)
    return (guard_pos[0]+guard_dir[0],guard_pos[1]+guard_dir[1]), guard_dir

visited = set()
while 0<= guard_pos[0]<len(map) and 0<=guard_pos[1]<len(map[0]):
    visited.add((guard_pos[0],guard_pos[1]))
    guard_pos, guard_dir = move_guard(guard_pos, guard_dir, rocks)
answer1= len(visited)

answer2 = 0
count = 0
obs = {x: set() for x in range(len(map))}
for x,y in visited:
    count+=1
    print(f"{count} / {answer1}")
    visited_new = {x_tmp: {y_tmp: set() for y_tmp in range(len(map[0]))} for x_tmp in range(len(map)) }
    if x == guard_pos_init[0] and y == guard_pos_init[1]:
        continue
    rocks_copy = copy.deepcopy(rocks)
    rocks_copy[x].add(y)
    guard_pos = guard_pos_init
    guard_dir = guard_dir_init
    while 0<= guard_pos[0]<len(map) and 0<=guard_pos[1]<len(map[0]):
        visited_new[guard_pos[0]][guard_pos[1]].add(guard_dir)
        guard_pos, guard_dir = move_guard(guard_pos, guard_dir, rocks_copy)
        # Detect loop
        if 0<= guard_pos[0]<len(map) and 0<=guard_pos[1]<len(map[0]) and guard_dir in visited_new[guard_pos[0]][guard_pos[1]]:
            answer2+=1
            obs[x].add(y)
            break

submit(answer1, part="a", day=day, year=year)
submit(answer2, part="b", day=day, year=year)