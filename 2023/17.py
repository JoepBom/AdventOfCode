from aocd.models import Puzzle
from aocd import submit
import os
from pprint import pprint

year=2023
day=17
part="a"
os.environ["AOC_SESSION"]="53616c7465645f5f38e9d0d82d146a56ab1d6712424f5e2e00846cd3f9a466e8a5599b36da85eb3c2c69a985a5774afe86260b5c528d679eeee49c1433aa183d"

puzzle = Puzzle(year,day)
input = puzzle.input_data.splitlines()

#(y,x): (d_y, d_x) steps_left, dist
saved_locations={((0,1), (0,1), 2): (int(input[0][1]),  ((0,0), (0,1), 3)), ((1,0), (1,0), 2, (0,0)): (int(input[1][0]),  ((0,0), (1,0), 3))}
visited_locations=set()
visited_nodes=set()
next_to_visit = ((0,1), (0,1), 2)


def update_saved_locations(instance_tuple, distance, prev_inst_tuple):
    for steps_left in range(0,instance_tuple[2]):
        if (instance_tuple[0], instance_tuple[1], steps_left) in saved_locations and saved_locations[(instance_tuple[0], instance_tuple[1], steps_left)][0]>=distance:
            del(saved_locations[(instance_tuple[0], instance_tuple[1], steps_left)])
    if instance_tuple in saved_locations.keys() and saved_locations[instance_tuple][0]<=distance:
        return
    saved_locations[instance_tuple] = (distance, prev_inst_tuple)
    return    


def analyze_node(node):
    location = node[0]
    direction = node[1]
    steps_left = node[2]
    if steps_left>0:
        next_loc=(location[0]+direction[0], location[1]+direction[1])
        if 0<=next_loc[0]<len(input) and 0<=next_loc[1]<len(input[0]):
            update_saved_locations((next_loc, direction, steps_left-1), saved_locations[node][0] + int(input[next_loc[0]][next_loc[1]]), node)
    new_direction=(direction[1], direction[0])
    next_loc=(location[0]+new_direction[0], location[1]+new_direction[1])
    if 0<=next_loc[0]<len(input) and 0<=next_loc[1]<len(input[0]):
        update_saved_locations((next_loc, new_direction, 2), saved_locations[node][0]+ int(input[next_loc[0]][next_loc[1]]), node)
    new_direction=(-direction[1], -direction[0])
    next_loc=(location[0]+new_direction[0], location[1]+new_direction[1])
    if 0<=next_loc[0]<len(input) and 0<=next_loc[1]<len(input[0]):
        update_saved_locations((next_loc, new_direction, 2), saved_locations[node][0]+ int(input[next_loc[0]][next_loc[1]]), node)
    del(saved_locations[node])
    visited_locations.add(node[0])
    visited_nodes.add(node)
    return


while next_to_visit is not None:
    # print(next_to_visit, saved_locations[next_to_visit])
    if next_to_visit[0]==(len(input)-1, len(input[0])-1):
        break
    analyze_node(next_to_visit)
    minimum_dist = min(j[0] for i,j in saved_locations.items() if i not in visited_nodes)
    minimum_nodes = [i for i,j in saved_locations.items() if i not in visited_nodes and j[0] == minimum_dist]
    if len(minimum_nodes)==0:
        next_to_visit=None
    else:
        next_to_visit=minimum_nodes[0]



# path_finding = [i for i in saved_locations if i[0]==(len(input)-1, len(input[0])-1)][0]
# path=[path_finding[0]]
# while True:
#     path_finding = saved_locations[path_finding][1]
#     path.append(path_finding[0])
#     if path_finding[0]==(0,0):
#         break

# print(path)
# for y in range(len(input)):
#     for x in range(len(input[0])):
#         if (y,x) in path:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()

# sol1=min(j[0] for i,j in saved_locations.items() if i[0]==(len(input)-1, len(input[0])-1))

sol1=saved_locations[next_to_visit][0]
print(sol1)
submit(sol1, part=part, day=day, year=year)