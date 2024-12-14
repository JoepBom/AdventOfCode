from aocd.models import Puzzle
from aocd import submit
import os
from pprint import pprint

year=2023
day=18
part="b"
os.environ["AOC_SESSION"]="53616c7465645f5f38e9d0d82d146a56ab1d6712424f5e2e00846cd3f9a466e8a5599b36da85eb3c2c69a985a5774afe86260b5c528d679eeee49c1433aa183d"

puzzle = Puzzle(year,day)
input = puzzle.input_data.splitlines()

input = [(i.split()[0], int(i.split()[1]), i.split()[2]) for i in input]
# pprint(input)

dir_map = {"0":"R", "1": "D", "2": "L", "3": 'U'}
input = [(dir_map[i[2][7]], int(i[2][2:7], 16)) for i in input]
direction_map={'U': (-1, 0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}
corner_map={'U': {'L': '7', 'R': 'F'}, 'D': {'L': 'J', 'R': 'L'}, 'L': {'U': 'L', 'D': 'F'}, 'R': {'U': 'J', 'D': '7'},}

def print_map(edges, corners):
    for y in range(-10, 11):
        for x in range(-10, 10+1):
            printed=False
            for key, val in corners.items():
                if y in val and x in val[y]:
                    print(key, end="")
                    printed=True
                    break
            if printed:
                continue
            if y in edges and x in edges[y]:
                print("#", end="")
            else:
                print(".", end="")
        print()

pos = (0,0)
edges = dict()
corners = {"L": dict(), "F": dict(),"7": dict(),"J": dict()}
all_corners=dict()
prev_dir = input[-1][0]
for instruction in input:
    dir=instruction[0]
    try:
        corners[corner_map[prev_dir][dir]][pos[0]].add(pos[1])
    except:
        corners[corner_map[prev_dir][dir]][pos[0]]={pos[1]}
    try:
        all_corners[pos[0]].add(pos[1])
    except:
        all_corners[pos[0]]={pos[1]}
    for j in range(instruction[1]):
        pos = (pos[0]+direction_map[dir][0], pos[1]+direction_map[dir][1])
        # print(dir, j, instruction[1]-1)
        if dir in {"U", "D"} and j!= instruction[1]-1:
            try:
                edges[pos[0]].add(pos[1])
            except:
                edges[pos[0]]={pos[1]}
    prev_dir=dir
edges = {key: sorted(list(val)) for key,val in edges.items()}
all_corners = {key1: sorted(list(val1)) for key1, val1 in all_corners.items()}
# pprint(corners)
# pprint(all_corners)
# pprint(edges)
sol1=0
prev_row_amount = None
for y in range(min(all_corners.keys()), max(all_corners.keys())+1):
    # print("evaluating y=", y)
    start_of_inside=None
    prev_corner=None
    count_row = 0
    if prev_row_amount is not None and y not in all_corners.keys():
        sol1+=prev_row_amount
        # print(y, "same as prev row: ", prev_row_amount)
        continue
    xs_of_corners = (set(all_corners[y]) if y in all_corners.keys() else set())
    xs_of_edges = (set(edges[y]) if y in edges.keys() else set())
    xs_of_interest = sorted(list(xs_of_corners | xs_of_edges))
    for x in xs_of_interest:
        # print(f"{x}: start_of_inside: {start_of_inside}")
        if x in xs_of_edges:
            if start_of_inside is None:
                start_of_inside = x
                continue
            count_row+= x-start_of_inside+1
            # print(count_row)
            start_of_inside=None
            continue
        if x in xs_of_corners:
            if prev_corner is None:
                if start_of_inside is not None:
                    count_row+= x-start_of_inside
                    # print(count_row)
                if y in corners["L"] and x in corners["L"][y]: 
                    prev_corner = (x,"L")
                elif y in corners["F"] and x in corners["F"][y]:
                    prev_corner = (x,"F")
            else:
                if y in corners["J"] and x in corners["J"][y]:
                    count_row+=x-prev_corner[0]+1
                    # print(count_row)
                    if prev_corner[1] == "F":
                        if start_of_inside is not None:
                            start_of_inside = None
                        else:
                            start_of_inside=x+1
                    else:
                        if start_of_inside is not None:
                            start_of_inside=x+1
                    prev_corner = None
                if y in corners["7"] and x in corners["7"][y]:
                    count_row+=x-prev_corner[0]+1
                    # print(count_row)
                    if prev_corner[1] == "L":
                        if start_of_inside is not None:
                            start_of_inside = None
                        else:
                            start_of_inside=x+1
                    else:
                        if start_of_inside is not None:
                            start_of_inside=x+1
                    prev_corner = None
    sol1+=count_row
    if y not in all_corners:
        prev_row_amount=count_row
    else:
        prev_row_amount = None
    # print(y, xs_of_corners, xs_of_edges, xs_of_interest, count_row)
                
print(sol1)

# print_map(edges, corners)


submit(sol1, part=part, day=day, year=year)