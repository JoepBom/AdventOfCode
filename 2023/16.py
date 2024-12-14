from aocd.models import Puzzle
from aocd import submit
import os

year=2023
day=16
part="a"
os.environ["AOC_SESSION"]="53616c7465645f5f38e9d0d82d146a56ab1d6712424f5e2e00846cd3f9a466e8a5599b36da85eb3c2c69a985a5774afe86260b5c528d679eeee49c1433aa183d"

puzzle = Puzzle(year,day)
input = puzzle.input_data.splitlines()


max_x = len(input[0])
max_y = len(input)

def get_energy(cur_points, dirs):
    visited_points = set()
    while len(cur_points)>0:
        indices_to_remove = set()
        points_to_add = []
        dirs_to_add = []
        for i, (cur_point, dir) in enumerate(zip(cur_points, dirs)):
            cur_point=(cur_point[0]+dir[0], cur_point[1]+dir[1])
            if cur_point[0]<0 or cur_point[0]>=max_x or cur_point[1]<0 or cur_point[1]>=max_y:
                indices_to_remove.add(i)
                continue
            cur_points[i]=cur_point
            point = input[cur_point[1]][cur_point[0]]
            if (tuple(cur_point), dir) in visited_points:
                indices_to_remove.add(i)
                continue
            visited_points.add((tuple(cur_point), dir))
            if point == ".":
                continue
            if point=="-" and dir[0]==0:
                points_to_add.append(cur_point)
                dirs_to_add.append((1,0))
                dirs[i]=(-1,0)
                continue
            if point=="|" and dir[1]==0:
                points_to_add.append(cur_point)
                dirs_to_add.append((0,1))
                dirs[i]=(0,-1)
                continue
            if point=="\\":
                dirs[i]=(dir[1], dir[0])
                continue
            if point=="/":
                dirs[i]=(-dir[1], -dir[0])
                continue
        for i in sorted(indices_to_remove, reverse=True):
            cur_points.pop(i)
            dirs.pop(i)
        for i in points_to_add:
            cur_points.append(i)
        for i in dirs_to_add:
            dirs.append(i)

    visited_points={i for i,_ in visited_points}

    return len(visited_points)

submit(get_energy([(-1,0)], [(1,0)]), part=part, day=day, year=year)

part="b"

energies = []
for i in range(max_x):
    energies.append(get_energy([(-1,i)], [(1,0)]))
    energies.append(get_energy([(max_x,i)], [(-1,0)]))
for i in range(max_y):
    energies.append(get_energy([(i,-1)], [(0,1)]))
    energies.append(get_energy([(i,max_y)], [(0,-1)]))

submit(max(energies), part=part, day=day, year=year)