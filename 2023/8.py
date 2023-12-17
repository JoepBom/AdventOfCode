import os
from aocd.models import Puzzle
from aocd import submit
from pprint import pprint
os.environ['AOC_SESSION'] = '53616c7465645f5f5274298a1513bd33b311098204a4e371d2880a4590e8a95748ea42877f6b28b349045dcc1fee6d10f00932890ec53d2fdfe8a068bae08242'

year=2023
day=8

puzzle = Puzzle(year=year, day=day)
input = puzzle.input_data.splitlines()
directions = input[0]
maps=input[2:]
paths={i[:3]:{"L":i[7:10], "R":i[12:15]} for i in maps}

part='a'

count=0
cur_pos="AAA"
while cur_pos!="ZZZ":
    cur_pos=paths[cur_pos][directions[count%len(directions)]]
    count+=1

ans1=count
submit(ans1, year=year, day=day, part=part)

part='b'

cur_positions=[i for i in paths.keys() if i[2]=="A"]
visited_points=[dict() for i in range(len(cur_positions))]
loops = [{"from":0, "length":0} for i in range(len(cur_positions))]
count=0
evaluated_indexes=[]
while len(evaluated_indexes)<len(cur_positions):
    dir_index = count%len(directions)
    count+=1
    new_positions=cur_positions
    for index, pos in enumerate(cur_positions):   
        if index in evaluated_indexes:
            continue
        new_positions[index]=paths[pos][directions[dir_index]]
        if (new_positions[index], dir_index) in visited_points[index]:
            loops[index]={"from":visited_points[index][(new_positions[index], dir_index)], "length":count-visited_points[index][(new_positions[index], dir_index)]}
            evaluated_indexes.append(index)
        else:
            visited_points[index][(new_positions[index], dir_index)]=count
    cur_positions=new_positions
    
def smallest_common_multiple(a,b):
    if a<b:
        c,d=b,a
    else:
        c,d=a,b
    while d!=0:
        c,d=d,c%d
    return a*b/c

def smallest_common_multiple_list(list):
    if len(list)==1:
        return list[0]
    else:
        return smallest_common_multiple(list[0], smallest_common_multiple_list(list[1:]))
    
submit(smallest_common_multiple_list([i["length"] for i in loops]), year=year, day=day, part=part)