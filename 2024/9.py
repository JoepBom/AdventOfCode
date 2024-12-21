from aocd.models import Puzzle
from aocd import submit
from itertools import combinations
from math import gcd
from pprint import pprint
year=2024
day=9
puzzle = Puzzle(year,day)

input = puzzle.input_data.splitlines()[0]
# input = puzzle.examples[0].input_data.splitlines()[0]

# print(input)

id_list = []

#(ID, start_nr, length)
count=0
for i, num in enumerate(input):
    if i%2==0:
        id_list.append((int(i/2), int(count), int(num)))
    else:
        id_list.append((None, int(count), int(num)))
    count+=int(num)

reversed_id_list = id_list[::-1]
filled_list = []

id_list_pointer = 0
for id, start_nr, bits_left in reversed_id_list:
    if id is None:
        continue
    if start_nr == id_list[id_list_pointer][1]:
        filled_list.append((id, start_nr, bits_left))
        id_list_pointer+=1
        break
    if start_nr < id_list[id_list_pointer][1]:
        break
    for index_id_list in range(id_list_pointer, len(id_list)):
        if start_nr <= id_list[index_id_list][1] or id == id_list[index_id_list][0]:
            filled_list.append((id, start_nr, bits_left))
            id_list_pointer+=1
            break
        if id_list[index_id_list][0] is not None:
            filled_list.append((id_list[index_id_list][0], id_list[index_id_list][1], id_list[index_id_list][2]))
            id_list_pointer+=1
            continue
        if id_list[index_id_list][2] < bits_left:
            filled_list.append((id, id_list[index_id_list][1], id_list[index_id_list][2]))
            bits_left-=id_list[index_id_list][2]
            id_list_pointer+=1
            continue
        if id_list[index_id_list][2] == bits_left:
            filled_list.append((id, id_list[index_id_list][1], id_list[index_id_list][2]))
            id_list_pointer+=1
            break
        if id_list[index_id_list][2] > bits_left:
            filled_list.append((id, id_list[index_id_list][1], bits_left))
            id_list[index_id_list] = (id_list[index_id_list][0], id_list[index_id_list][1]+bits_left, id_list[index_id_list][2]-bits_left)
            break

# pprint(filled_list)

filled_score = [i[0]*j for i in filled_list for j in range(i[1], i[1]+i[2])]
print(filled_score)
submit(sum(filled_score), part="a", day=day, year=year)
# submit(len(antinodes2), part="b", day=day, year=year)


input = puzzle.input_data.splitlines()[0]
# input = puzzle.examples[0].input_data.splitlines()[0]

# print(input)

id_list = []

#(ID, start_nr, length)
count=0
for i, num in enumerate(input):
    if i%2==0:
        id_list.append((int(i/2), int(count), int(num)))
    else:
        id_list.append((None, int(count), int(num)))
    count+=int(num)

reversed_id_list = id_list[::-1]
filled_list = []

for id, start_nr, bits_left in reversed_id_list:
    if id is None:
        continue
    if len(filled_list)>0 and id == filled_list[-1][0]:
        break
    for index_id_list in range(0, len(id_list)):
        if start_nr <= id_list[index_id_list][1] or id == id_list[index_id_list][0]:
            filled_list.append((id, start_nr, bits_left))
            break
        if id_list[index_id_list][0] is not None:
            continue
        if id_list[index_id_list][2] < bits_left:
            continue
        if id_list[index_id_list][2] == bits_left:
            filled_list.append((id, id_list[index_id_list][1], id_list[index_id_list][2]))
            id_list[index_id_list] = (id_list[index_id_list][0], id_list[index_id_list][1]+bits_left, id_list[index_id_list][2]-bits_left)
            break
        if id_list[index_id_list][2] > bits_left:
            filled_list.append((id, id_list[index_id_list][1], bits_left))
            id_list[index_id_list] = (id_list[index_id_list][0], id_list[index_id_list][1]+bits_left, id_list[index_id_list][2]-bits_left)
            break
pprint(filled_list)
filled_score = [i[0]*j for i in filled_list for j in range(i[1], i[1]+i[2]) if i[0] is not None]
print(sum(filled_score))
# submit(sum(filled_score), part="a", day=day, year=year)
submit(sum(filled_score), part="b", day=day, year=year)
