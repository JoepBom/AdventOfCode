def print_with_dir(mapping):
    for x in mapping:
        for y in mapping[x]:
            if len(mapping[x][y]) == 0:
                print(".", end="")
            hor, ver = False, False
            if ((1,0) in mapping[x][y] or (-1,0) in mapping[x][y]):
                ver = True
            if ((0,1) in mapping[x][y] or (0,-1) in mapping[x][y]):
                hor = True
            if hor and ver:
                print("+", end="")
            elif hor:
                print("-", end="")
            elif ver:
                print("|", end="")
        print()
    print()

from aocd.models import Puzzle
from aocd import submit
import copy

year=2024
day=6
puzzle = Puzzle(year,day)

map = puzzle.input_data.splitlines()
# map = puzzle.examples[0].input_data.splitlines()
rocks = {x: set() for x in range(len(map))}
for x in range(len(map)):
    for y in range(len(map[0])):
        if map[x][y] == "#":
            rocks[x].add(y)
        elif map[x][y] in (">", "<","^","v"):
            guard_pos_init = (x,y)
            guard_symb = map[x][y]

guard_dir_init = ((0,1) if guard_symb == ">"else (0,-1) if guard_symb == "<" else (1,0) if guard_symb == "v" else (-1,0))

guard_pos = guard_pos_init
guard_dir = guard_dir_init

def update_loop_options(shadow_pos, shadow_dir, rocks, loop_options):
    while 0<= shadow_pos[0]<len(map) and 0<=shadow_pos[1]<len(map[0]) and shadow_dir not in loop_options[shadow_pos[0]][shadow_pos[1]]:
        if shadow_pos[0]+shadow_dir[1] in rocks and shadow_pos[1] -shadow_dir[0] in rocks[shadow_pos[0]+shadow_dir[1]]:
            # turn possible
            update_loop_options(shadow_pos, (-shadow_dir[1], shadow_dir[0]), rocks, loop_options)
        if shadow_pos[0]+shadow_dir[0] in rocks and shadow_pos[1] +shadow_dir[1] in rocks[shadow_pos[0]+shadow_dir[0]]:
            # rock hit
            break
        loop_options[shadow_pos[0]][shadow_pos[1]].add(shadow_dir)
        shadow_pos = (shadow_pos[0]+shadow_dir[0], shadow_pos[1]+shadow_dir[1])
    return

def turn_guard(guard_pos, guard_dir, rocks):
    if guard_pos[0]+guard_dir[0] in rocks and guard_pos[1]+guard_dir[1] in rocks[guard_pos[0]+guard_dir[0]]:
        guard_dir = (guard_dir[1], -guard_dir[0])
        update_loop_options(guard_pos, (-guard_dir[0], -guard_dir[1]), rocks, loop_options_with_dir)
        return turn_guard(guard_pos, guard_dir, rocks)
    return guard_dir


outside_paths_with_dir = {x: {y: set() for y in range(len(map[0]))} for x in range(len(map)) }
def find_initial_loop_options(x,y,dir, rocks):
    if x in rocks and y in rocks[x]:
        return
    shadow_pos = (x,y)
    shadow_dir = dir
    while 0<= shadow_pos[0]<len(map) and 0<=shadow_pos[1]<len(map[0]) and shadow_dir not in outside_paths_with_dir[shadow_pos[0]][shadow_pos[1]]:
        if shadow_pos[0]+shadow_dir[1] in rocks and shadow_pos[1] -shadow_dir[0] in rocks[shadow_pos[0]+shadow_dir[1]]:
            # turn possible
            update_loop_options(shadow_pos, (-shadow_dir[1], shadow_dir[0]), rocks, outside_paths_with_dir)
        if shadow_pos[0]+shadow_dir[0] in rocks and shadow_pos[1] +shadow_dir[1] in rocks[shadow_pos[0]+shadow_dir[0]]:
            # rock hit
            break
        outside_paths_with_dir[shadow_pos[0]][shadow_pos[1]].add(shadow_dir)
        shadow_pos = (shadow_pos[0]+shadow_dir[0], shadow_pos[1]+shadow_dir[1]) 


for x in range(0,len(map)):
    for y,dir in ((0,(0,1)), (len(map[0]), (0,-1))):
        find_initial_loop_options(x,y,dir,rocks)
for y in range(0,len(map[0])):
    for x,dir in ((0,(1,0)), (len(map), (-1,0))):
        find_initial_loop_options(x,y,dir,rocks)

# print(rocks)
answer2=0
visited = {x: set() for x in range(len(map))}
loop_options_with_dir = {x: {y: set() for y in range(len(map[0]))} for x in range(len(map)) }
obs_pos = {x: set() for x in range(len(map))}

for x in range(len(map)):
    for y in range(len(map[0])):
        for dir in ((0,1), (0,-1), (1,0), (-1,0)):
            if not(x in rocks and y in rocks[x]) and not (x in outside_paths_with_dir and y in outside_paths_with_dir[x] and dir not in outside_paths_with_dir[x][y]):
                loop_options_with_dir[x][y].add(dir)

print_with_dir(loop_options_with_dir)
update_loop_options(guard_pos, (-guard_dir[0], -guard_dir[1]), rocks, loop_options_with_dir)

while 0<= guard_pos[0]<len(map) and 0<=guard_pos[1]<len(map[0]):
    visited[guard_pos[0]].add(guard_pos[1])
    if guard_pos[0]+guard_dir[0] in rocks and guard_pos[1]+guard_dir[1] in rocks[guard_pos[0]+guard_dir[0]]:
        # rock hit
        guard_dir = turn_guard(guard_pos, guard_dir, rocks)
    if (-guard_dir[1], guard_dir[0]) in loop_options_with_dir[guard_pos[0]][guard_pos[1]] and 0<= guard_pos[0]+guard_dir[0]<len(map) and 0<=guard_pos[1]+guard_dir[0]<len(map[0]):
        obs_pos[guard_pos[0]+guard_dir[0]].add(guard_pos[1]+guard_dir[1])
    guard_pos = (guard_pos[0]+guard_dir[0], guard_pos[1]+guard_dir[1])
    # print(guard_pos, guard_dir)
answer1 = sum(len(visited[x]) for x in visited)

def move_guard(guard_pos, guard_dir, rocks):
    if guard_pos[0]+guard_dir[0] in rocks and guard_pos[1]+guard_dir[1] in rocks[guard_pos[0]+guard_dir[0]]:
        guard_dir = (guard_dir[1], -guard_dir[0])
        return move_guard(guard_pos, guard_dir, rocks)
    return (guard_pos[0]+guard_dir[0],guard_pos[1]+guard_dir[1]), guard_dir


count_max = sum(len(obs_pos[x]) for x in obs_pos)
count = 0
obs = {x: set() for x in range(len(map))}
for x in obs_pos:
    for y in obs_pos[x]:
        count+=1
        print(f"{count} / {count_max}")
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
            if 0<= guard_pos[0]<len(map) and 0<=guard_pos[1]<len(map[0]) and guard_dir in visited_new[guard_pos[0]][guard_pos[1]]:
                answer2+=1
                obs[x].add(y)
                break

answer2 = sum(len(obs[x]) for x in obs)

print_with_dir(loop_options_with_dir)

def print_without_dir(mapping):
    for x in mapping:
        for y in range(len(map[0])):
            if y in mapping[x]:
                print("O", end="")
            else:
                print(".",end="")
        print()

print()
print_without_dir(obs_pos)

print(answer2)

print()
submit(answer1, part="a", day=day, year=year)
submit(answer2, part="b", day=day, year=year)